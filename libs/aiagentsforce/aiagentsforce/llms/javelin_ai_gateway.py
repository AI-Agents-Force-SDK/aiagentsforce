from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.llms import JavelinAIGateway
    from aiagentsforce_community.llms.javelin_ai_gateway import Params

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "JavelinAIGateway": "aiagentsforce_community.llms",
    "Params": "aiagentsforce_community.llms.javelin_ai_gateway",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "JavelinAIGateway",
    "Params",
]
