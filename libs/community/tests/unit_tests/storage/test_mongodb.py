"""Light weight unit test that attempts to import MongodbStore.

The actual code is tested in integration tests.

This test is intended to catch errors in the import process.
"""


def test_import_storage() -> None:
    """Attempt to import storage modules."""
    from aiagentsforce_community.storage.mongodb import MongoDBStore  # noqa
