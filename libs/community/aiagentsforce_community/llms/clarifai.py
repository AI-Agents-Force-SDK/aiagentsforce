import logging
from typing import Any, Dict, List, Optional

from aiagentsforce_core.callbacks import CallbackManagerForLLMRun
from aiagentsforce_core.language_models.llms import LLM
from aiagentsforce_core.outputs import Generation, LLMResult
from aiagentsforce_core.utils import pre_init
from pydantic import ConfigDict, Field

from aiagentsforce_community.llms.utils import enforce_stop_tokens

logger = logging.getLogger(__name__)


EXAMPLE_URL = "https://clarifai.com/openai/chat-completion/models/GPT-4"


class Clarifai(LLM):
    """Clarifai large language models.

    To use, you should have an account on the Clarifai platform,
    the ``clarifai`` python package installed, and the
    environment variable ``CLARIFAI_PAT`` set with your PAT key,
    or pass it as a named parameter to the constructor.

    Example:
        .. code-block:: python

            from aiagentsforce_community.llms import Clarifai
            clarifai_llm = Clarifai(user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID)
                             (or)
            clarifai_llm = Clarifai(model_url=EXAMPLE_URL)
    """

    model_url: Optional[str] = None
    """Model url to use."""
    model_id: Optional[str] = None
    """Model id to use."""
    model_version_id: Optional[str] = None
    """Model version id to use."""
    app_id: Optional[str] = None
    """Clarifai application id to use."""
    user_id: Optional[str] = None
    """Clarifai user id to use."""
    pat: Optional[str] = Field(default=None, exclude=True)  #: :meta private:
    """Clarifai personal access token to use."""
    token: Optional[str] = Field(default=None, exclude=True)  #: :meta private:
    """Clarifai session token to use."""
    model: Any = Field(default=None, exclude=True)  #: :meta private:
    api_base: str = "https://api.clarifai.com"

    model_config = ConfigDict(
        extra="forbid",
    )

    @pre_init
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that we have all required info to access Clarifai
        platform and python package exists in environment."""
        try:
            from clarifai.client.model import Model
        except ImportError:
            raise ImportError(
                "Could not import clarifai python package. "
                "Please install it with `pip install clarifai`."
            )
        user_id = values.get("user_id")
        app_id = values.get("app_id")
        model_id = values.get("model_id")
        model_version_id = values.get("model_version_id")
        model_url = values.get("model_url")
        api_base = values.get("api_base")
        pat = values.get("pat")
        token = values.get("token")

        values["model"] = Model(
            url=model_url,
            app_id=app_id,
            user_id=user_id,
            model_version=dict(id=model_version_id),
            pat=pat,
            token=token,
            model_id=model_id,
            base_url=api_base,
        )

        return values

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling Clarifai API."""
        return {}

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters."""
        return {
            **{
                "model_url": self.model_url,
                "user_id": self.user_id,
                "app_id": self.app_id,
                "model_id": self.model_id,
            }
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "clarifai"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        inference_params: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> str:
        """Call out to Clarfai's PostModelOutputs endpoint.

        Args:
            prompt: The prompt to pass into the model.
            stop: Optional list of stop words to use when generating.

        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python

                response = clarifai_llm.invoke("Tell me a joke.")
        """

        try:
            (inference_params := {}) if inference_params is None else inference_params
            predict_response = self.model.predict_by_bytes(
                bytes(prompt, "utf-8"),
                input_type="text",
                inference_params=inference_params,
            )
            text = predict_response.outputs[0].data.text.raw
            if stop is not None:
                text = enforce_stop_tokens(text, stop)

        except Exception as e:
            logger.error(f"Predict failed, exception: {e}")

        return text

    def _generate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        inference_params: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> LLMResult:
        """Run the LLM on the given prompt and input."""

        # TODO: add caching here.
        try:
            from clarifai.client.input import Inputs
        except ImportError:
            raise ImportError(
                "Could not import clarifai python package. "
                "Please install it with `pip install clarifai`."
            )

        generations = []
        batch_size = 32
        input_obj = Inputs.from_auth_helper(self.model.auth_helper)
        try:
            for i in range(0, len(prompts), batch_size):
                batch = prompts[i : i + batch_size]
                input_batch = [
                    input_obj.get_text_input(input_id=str(id), raw_text=inp)
                    for id, inp in enumerate(batch)
                ]
                (
                    inference_params := {}
                ) if inference_params is None else inference_params
                predict_response = self.model.predict(
                    inputs=input_batch, inference_params=inference_params
                )

            for output in predict_response.outputs:
                if stop is not None:
                    text = enforce_stop_tokens(output.data.text.raw, stop)
                else:
                    text = output.data.text.raw

                generations.append([Generation(text=text)])

        except Exception as e:
            logger.error(f"Predict failed, exception: {e}")

        return LLMResult(generations=generations)