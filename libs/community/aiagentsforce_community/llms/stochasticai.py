import logging
import time
from typing import Any, Dict, List, Mapping, Optional

import requests
from aiagentsforce_core.callbacks import CallbackManagerForLLMRun
from aiagentsforce_core.language_models.llms import LLM
from aiagentsforce_core.utils import convert_to_secret_str, get_from_dict_or_env, pre_init
from pydantic import ConfigDict, Field, SecretStr, model_validator

from aiagentsforce_community.llms.utils import enforce_stop_tokens

logger = logging.getLogger(__name__)


class StochasticAI(LLM):
    """StochasticAI large language models.

    To use, you should have the environment variable ``STOCHASTICAI_API_KEY``
    set with your API key.

    Example:
        .. code-block:: python

            from aiagentsforce_community.llms import StochasticAI
            stochasticai = StochasticAI(api_url="")
    """

    api_url: str = ""
    """Model name to use."""

    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Holds any model parameters valid for `create` call not
    explicitly specified."""

    stochasticai_api_key: Optional[SecretStr] = None

    model_config = ConfigDict(
        extra="forbid",
    )

    @model_validator(mode="before")
    @classmethod
    def build_extra(cls, values: Dict[str, Any]) -> Any:
        """Build extra kwargs from additional params that were passed in."""
        all_required_field_names = set(list(cls.model_fields.keys()))

        extra = values.get("model_kwargs", {})
        for field_name in list(values):
            if field_name not in all_required_field_names:
                if field_name in extra:
                    raise ValueError(f"Found {field_name} supplied twice.")
                logger.warning(
                    f"""{field_name} was transferred to model_kwargs.
                    Please confirm that {field_name} is what you intended."""
                )
                extra[field_name] = values.pop(field_name)
        values["model_kwargs"] = extra
        return values

    @pre_init
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key exists in environment."""
        stochasticai_api_key = convert_to_secret_str(
            get_from_dict_or_env(values, "stochasticai_api_key", "STOCHASTICAI_API_KEY")
        )
        values["stochasticai_api_key"] = stochasticai_api_key
        return values

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            **{"endpoint_url": self.api_url},
            **{"model_kwargs": self.model_kwargs},
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "stochasticai"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Call out to StochasticAI's complete endpoint.

        Args:
            prompt: The prompt to pass into the model.
            stop: Optional list of stop words to use when generating.

        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python

                response = StochasticAI("Tell me a joke.")
        """
        params = self.model_kwargs or {}
        params = {**params, **kwargs}
        response_post = requests.post(
            url=self.api_url,
            json={"prompt": prompt, "params": params},
            headers={
                "apiKey": f"{self.stochasticai_api_key.get_secret_value()}",  # type: ignore[union-attr]
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        response_post.raise_for_status()
        response_post_json = response_post.json()
        completed = False
        while not completed:
            response_get = requests.get(
                url=response_post_json["data"]["responseUrl"],
                headers={
                    "apiKey": f"{self.stochasticai_api_key.get_secret_value()}",  # type: ignore[union-attr]
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
            )
            response_get.raise_for_status()
            response_get_json = response_get.json()["data"]
            text = response_get_json.get("completion")
            completed = text is not None
            time.sleep(0.5)
        text = text[0]
        if stop is not None:
            # I believe this is required since the stop tokens
            # are not enforced by the model parameters
            text = enforce_stop_tokens(text, stop)
        return text