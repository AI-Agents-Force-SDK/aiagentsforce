from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.document_loaders import (
        AirbyteCDKLoader,
        AirbyteGongLoader,
        AirbyteHubspotLoader,
        AirbyteSalesforceLoader,
        AirbyteShopifyLoader,
        AirbyteStripeLoader,
        AirbyteTypeformLoader,
        AirbyteZendeskSupportLoader,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "AirbyteCDKLoader": "aiagentsforce_community.document_loaders",
    "AirbyteHubspotLoader": "aiagentsforce_community.document_loaders",
    "AirbyteStripeLoader": "aiagentsforce_community.document_loaders",
    "AirbyteTypeformLoader": "aiagentsforce_community.document_loaders",
    "AirbyteZendeskSupportLoader": "aiagentsforce_community.document_loaders",
    "AirbyteShopifyLoader": "aiagentsforce_community.document_loaders",
    "AirbyteSalesforceLoader": "aiagentsforce_community.document_loaders",
    "AirbyteGongLoader": "aiagentsforce_community.document_loaders",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "AirbyteCDKLoader",
    "AirbyteHubspotLoader",
    "AirbyteStripeLoader",
    "AirbyteTypeformLoader",
    "AirbyteZendeskSupportLoader",
    "AirbyteShopifyLoader",
    "AirbyteSalesforceLoader",
    "AirbyteGongLoader",
]
