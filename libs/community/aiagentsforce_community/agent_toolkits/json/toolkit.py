from __future__ import annotations

from typing import List

from aiagentsforce_core.tools import BaseTool
from aiagentsforce_core.tools.base import BaseToolkit

from aiagentsforce_community.tools.json.tool import (
    JsonGetValueTool,
    JsonListKeysTool,
    JsonSpec,
)


class JsonToolkit(BaseToolkit):
    """Toolkit for interacting with a JSON spec.

    Parameters:
        spec: The JSON spec.
    """

    spec: JsonSpec

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [
            JsonListKeysTool(spec=self.spec),
            JsonGetValueTool(spec=self.spec),
        ]
