import pytest
from aiagentsforce_core.utils import check_package_version


def test_check_package_version_pass() -> None:
    check_package_version("PyYAML", gte_version="5.4.1")


def test_check_package_version_fail() -> None:
    with pytest.raises(ValueError):
        check_package_version("PyYAML", lt_version="5.4.1")
