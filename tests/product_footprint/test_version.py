import pytest

from pathfinder_framework.product_footprint.version import Version


def test_init_with_valid_version():
    version = Version(1)
    assert version.version == 1


def test_init_with_invalid_type():
    with pytest.raises(ValueError):
        Version("1")


@pytest.mark.parametrize("version", [-1, 2**31])
def test_init_with_version_out_of_range(version):
    with pytest.raises(ValueError):
        Version(version)


def test_equality():
    version1 = Version(1)
    version2 = Version(1)
    assert version1 == version2

    version3 = Version(2)
    assert version1 != version3


def test_get_latest_version():
    version1 = Version(1)
    version2 = Version(2)
    version3 = Version(3)

    assert Version.get_latest_version(version1, version2, version3) == version3


def test_get_latest_version_with_one_version():
    version = Version(1)

    assert Version.get_latest_version(version) == version


def test_get_latest_version_with_no_versions():
    with pytest.raises(ValueError):
        Version.get_latest_version()


def test_get_latest_version_with_invalid_arguments():
    with pytest.raises(ValueError):
        Version.get_latest_version(Version(1), "2", Version(3))
