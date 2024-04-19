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
