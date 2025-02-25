"""Tool for the Arxiv API."""

from typing import Optional, Type

from aiagentsforce_core.callbacks import CallbackManagerForToolRun
from aiagentsforce_core.tools import BaseTool
from pydantic import BaseModel, Field

from aiagentsforce_community.utilities.arxiv import ArxivAPIWrapper


class ArxivInput(BaseModel):
    """Input for the Arxiv tool."""

    query: str = Field(description="search query to look up")


class ArxivQueryRun(BaseTool):  # type: ignore[override, override]
    """Tool that searches the Arxiv API."""

    name: str = "arxiv"
    description: str = (
        "A wrapper around Arxiv.org "
        "Useful for when you need to answer questions about Physics, Mathematics, "
        "Computer Science, Quantitative Biology, Quantitative Finance, Statistics, "
        "Electrical Engineering, and Economics "
        "from scientific articles on arxiv.org. "
        "Input should be a search query."
    )
    api_wrapper: ArxivAPIWrapper = Field(default_factory=ArxivAPIWrapper)  # type: ignore[arg-type]
    args_schema: Type[BaseModel] = ArxivInput

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Arxiv tool."""
        return self.api_wrapper.run(query)
