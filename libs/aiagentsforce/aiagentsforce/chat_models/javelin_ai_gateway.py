from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.chat_models.javelin_ai_gateway import (
        ChatJavelinAIGateway,
        ChatParams,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "ChatJavelinAIGateway": "aiagentsforce_community.chat_models.javelin_ai_gateway",
    "ChatParams": "aiagentsforce_community.chat_models.javelin_ai_gateway",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "ChatJavelinAIGateway",
    "ChatParams",
]
