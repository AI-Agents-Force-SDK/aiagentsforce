from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.retrievers import (
        GoogleCloudEnterpriseSearchRetriever,
        GoogleVertexAIMultiTurnSearchRetriever,
        GoogleVertexAISearchRetriever,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "GoogleVertexAISearchRetriever": "aiagentsforce_community.retrievers",
    "GoogleVertexAIMultiTurnSearchRetriever": "aiagentsforce_community.retrievers",
    "GoogleCloudEnterpriseSearchRetriever": "aiagentsforce_community.retrievers",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "GoogleVertexAISearchRetriever",
    "GoogleVertexAIMultiTurnSearchRetriever",
    "GoogleCloudEnterpriseSearchRetriever",
]