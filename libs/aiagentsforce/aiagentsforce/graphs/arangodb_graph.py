from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.graphs import ArangoGraph
    from aiagentsforce_community.graphs.arangodb_graph import get_arangodb_client

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "ArangoGraph": "aiagentsforce_community.graphs",
    "get_arangodb_client": "aiagentsforce_community.graphs.arangodb_graph",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "ArangoGraph",
    "get_arangodb_client",
]
