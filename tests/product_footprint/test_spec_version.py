import pytest

from pathfinder_framework.product_footprint.spec_version import SpecVersion


def test_init_with_valid_version():
    version = SpecVersion(1)
    assert version.version == 1


def test_init_with_invalid_type():
    with pytest.raises(ValueError):
        SpecVersion("1")


@pytest.mark.parametrize("version", [-1, 2**31])
def test_init_with_version_out_of_range(version):
    with pytest.raises(ValueError):
        SpecVersion(version)


def test_equality():
    version1 = SpecVersion(1)
    version2 = SpecVersion(1)
    assert version1 == version2

    version3 = SpecVersion(2)
    assert version1 != version3


def test_get_latest_version():
    version1 = SpecVersion(1)
    version2 = SpecVersion(2)
    version3 = SpecVersion(3)

    assert SpecVersion.get_latest_version(version1, version2, version3) == version3


def test_get_latest_version_with_one_version():
    version = SpecVersion(1)

    assert SpecVersion.get_latest_version(version) == version


def test_get_latest_version_with_no_versions():
    with pytest.raises(ValueError):
        SpecVersion.get_latest_version()


def test_get_latest_version_with_invalid_arguments():
    with pytest.raises(ValueError):
        SpecVersion.get_latest_version(SpecVersion(1), "2", SpecVersion(3))
