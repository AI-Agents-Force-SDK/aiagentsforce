from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.document_loaders import WhatsAppChatLoader
    from aiagentsforce_community.document_loaders.whatsapp_chat import concatenate_rows

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "concatenate_rows": "aiagentsforce_community.document_loaders.whatsapp_chat",
    "WhatsAppChatLoader": "aiagentsforce_community.document_loaders",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "concatenate_rows",
    "WhatsAppChatLoader",
]