"""MultiOn agent."""

from __future__ import annotations

from typing import List

from aiagentsforce_core.tools import BaseTool
from aiagentsforce_core.tools.base import BaseToolkit
from pydantic import ConfigDict

from aiagentsforce_community.tools.multion.close_session import MultionCloseSession
from aiagentsforce_community.tools.multion.create_session import MultionCreateSession
from aiagentsforce_community.tools.multion.update_session import MultionUpdateSession


class MultionToolkit(BaseToolkit):
    """Toolkit for interacting with the Browser Agent.

    **Security Note**: This toolkit contains tools that interact with the
        user's browser via the multion API which grants an agent
        access to the user's browser.

        Please review the documentation for the multion API to understand
        the security implications of using this toolkit.

        See https://docs.aiagentsforce.com/docs/security for more information.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [MultionCreateSession(), MultionUpdateSession(), MultionCloseSession()]
