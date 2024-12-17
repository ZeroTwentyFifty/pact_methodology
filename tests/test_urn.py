import pytest

from pact_methodology.urn import URN, CompanyId, ProductId


@pytest.mark.parametrize(
    "urn_string",
    [
        "urn:isbn:978-0-596-52932-1",
        "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
        "urn:ietf:rfc:2648",
        "urn:example:foo-bar",
    ],
)
def test_valid_urn(urn_string):
    """Test initialization with valid URN strings."""
    urn = URN(value=urn_string)
    assert urn.value == urn_string


@pytest.mark.parametrize(
    "urn_string",
    [
        "not-a-valid-urn",
        "urn:invalid",
        "urn:example: invalid",
        "urn::double-colon::",
    ],
)
def test_invalid_urn_format(urn_string):
    """Test initialization with invalid URN strings."""
    with pytest.raises(ValueError, match="Value must be a valid URN"):
        URN(value=urn_string)


def test_str_representation():
    """Test string representation of URN."""
    urn_string = "urn:isbn:978-0-596-52932-1"
    urn = URN(value=urn_string)
    assert str(urn) == urn_string


def test_repr_representation():
    """Test representation of URN."""
    urn_string = "urn:isbn:978-0-596-52932-1"
    urn = URN(value=urn_string)
    assert repr(urn) == f"URN(value='{urn_string}')"


def test_hash():
    """Test hash functionality of URN."""
    urn_string = "urn:isbn:978-0-596-52932-1"
    urn = URN(value=urn_string)
    assert hash(urn) == hash(urn_string)


def test_equality_same_instance():
    """Test equality of the same URN instance."""
    urn = URN(value="urn:isbn:978-0-596-52932-1")
    assert urn == urn


def test_equality_different_instances():
    """Test equality of different URN instances with the same value."""
    urn1 = URN(value="urn:isbn:978-0-596-52932-1")
    urn2 = URN(value="urn:isbn:978-0-596-52932-1")
    assert urn1 == urn2


def test_inequality_different_values():
    """Test inequality of URN instances with different values."""
    urn1 = URN(value="urn:isbn:978-0-596-52932-1")
    urn2 = URN(value="urn:isbn:978-1-56619-909-4")
    assert urn1 != urn2


def test_inequality_with_non_urn():
    """Test inequality of URN instance with non-URN object."""
    urn = URN(value="urn:isbn:978-0-596-52932-1")
    assert urn != "urn:isbn:978-0-596-52932-1"
    assert urn != 123
    assert urn != None


def test_hash_consistency():
    """Test hash consistency across different instances with the same value."""
    urn1 = URN(value="urn:isbn:978-0-596-52932-1")
    urn2 = URN(value="urn:isbn:978-0-596-52932-1")
    assert hash(urn1) == hash(urn2)


def test_hash_inequality():
    """Test hash inequality for different URN values."""
    urn1 = URN(value="urn:isbn:978-0-596-52932-1")
    urn2 = URN(value="urn:isbn:978-1-56619-909-4")
    assert hash(urn1) != hash(urn2)

import pytest

from pact_methodology.urn import CompanyId


@pytest.mark.parametrize(
    "company_id",
    [
        "urn:pathfinder:company:customcode:buyer-assigned:acme-corp",
        "urn:pathfinder:company:customcode:buyer-assigned:12345",
        "urn:pathfinder:company:customcode:vendor-assigned:acme-corp",
        "urn:pathfinder:company:customcode:vendor-assigned:12345",
    ],
)
def test_valid_company_ids(company_id):
    """Test initialization with valid CompanyId strings."""
    cid = CompanyId(value=company_id)
    assert cid.value == company_id


@pytest.mark.parametrize(
    "company_id",
    [
        "urn:pathfinder:company:customcode:vendor-assigned:",
        "urn:pathfinder:company:customcode:invalid-type:12345",
        "urn:pathfinder:company:customcode:buyer-assigned:",
    ],
)
def test_invalid_company_ids(company_id):
    """Test initialization with invalid CompanyId strings."""
    with pytest.raises(ValueError, match="CompanyId does not conform to the required format"):
        CompanyId(value=company_id)


def test_company_id_inherits_urn_validation():
    """Test that CompanyId inherits URN validation."""
    with pytest.raises(ValueError, match="Value must be a valid URN"):
        CompanyId(value="invalid-urn")


def test_company_id_str_representation():
    """Test string representation of CompanyId."""
    company_id = "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
    cid = CompanyId(value=company_id)
    assert str(cid) == company_id


def test_company_id_repr_representation():
    """Test representation of CompanyId."""
    company_id = "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
    cid = CompanyId(value=company_id)
    assert repr(cid) == f"CompanyId(value='{company_id}')"


def test_company_id_hash():
    """Test hash functionality of CompanyId."""
    company_id = "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
    cid = CompanyId(value=company_id)
    assert hash(cid) == hash(company_id)


def test_company_id_equality_same_instance():
    """Test equality of the same CompanyId instance."""
    cid = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    assert cid == cid


def test_company_id_equality_different_instances():
    """Test equality of different CompanyId instances with the same value."""
    cid1 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    cid2 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    assert cid1 == cid2


def test_company_id_inequality_different_values():
    """Test inequality of CompanyId instances with different values."""
    cid1 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    cid2 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:other-corp")
    assert cid1 != cid2


def test_company_id_inequality_with_non_company_id():
    """Test inequality of CompanyId instance with non-CompanyId object."""
    cid = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    assert cid != "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
    assert cid != 123
    assert cid != None


def test_company_id_hash_consistency():
    """Test hash consistency across different CompanyId instances with the same value."""
    cid1 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    cid2 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    assert hash(cid1) == hash(cid2)


def test_company_id_hash_inequality():
    """Test hash inequality for different CompanyId values."""
    cid1 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    cid2 = CompanyId(value="urn:pathfinder:company:customcode:buyer-assigned:other-corp")
    assert hash(cid1) != hash(cid2)