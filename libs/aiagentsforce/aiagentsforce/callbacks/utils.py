from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.callbacks.utils import (
        BaseMetadataCallbackHandler,
        _flatten_dict,
        flatten_dict,
        hash_string,
        import_pandas,
        import_spacy,
        import_textstat,
        load_json,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "import_spacy": "aiagentsforce_community.callbacks.utils",
    "import_pandas": "aiagentsforce_community.callbacks.utils",
    "import_textstat": "aiagentsforce_community.callbacks.utils",
    "_flatten_dict": "aiagentsforce_community.callbacks.utils",
    "flatten_dict": "aiagentsforce_community.callbacks.utils",
    "hash_string": "aiagentsforce_community.callbacks.utils",
    "load_json": "aiagentsforce_community.callbacks.utils",
    "BaseMetadataCallbackHandler": "aiagentsforce_community.callbacks.utils",
}

_import_attribute = create_importer(__file__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "import_spacy",
    "import_pandas",
    "import_textstat",
    "_flatten_dict",
    "flatten_dict",
    "hash_string",
    "load_json",
    "BaseMetadataCallbackHandler",
]
