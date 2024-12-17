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

def test_valid_company_ids():
    valid_ids = [
        "urn:pathfinder:company:customcode:buyer-assigned:acme-corp",
        "urn:pathfinder:company:customcode:vendor-assigned:12345",
    ]
    for cid in valid_ids:
        CompanyId(value=cid)


def test_invalid_company_ids():
    invalid_ids = [
        "urn:pathfinder:company:customcode:buyer-assigned:bad code",
        "urn:pathfinder:company:customcode:vendor-assigned:",
        "not-a-company-id",
    ]
    for cid in invalid_ids:
        with pytest.raises(ValueError):
            CompanyId(value=cid)


@pytest.mark.parametrize(
    "product_id",
    [
        "urn:pathfinder:product:customcode:buyer-assigned:acme-product",
        "urn:pathfinder:product:customcode:vendor-assigned:12345",
        "urn:pathfinder:product:id:cas:64-17-5",
        "urn:pathfinder:product:id:cas:1067-08-9",
        "urn:pathfinder:product:id:cas:2306877-20-1",
        "urn:pathfinder:product:id:iupac-inchi:1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)",
    ],
)
def test_valid_product_ids(product_id):
    pid = ProductId(value=product_id)
    assert pid.value == product_id


@pytest.mark.parametrize(
    "product_id",
    [
        "urn:pathfinder:product:customcode:buyer-assigned:acme product",
        "urn:pathfinder:product:customcode:vendor-assigned:",
        "urn:pathfinder:product:id:cas:17-5",
        "urn:pathfinder:product:id:cas:1345678-08-9",
    ],
)
def test_invalid_product_ids(product_id):
    with pytest.raises(ValueError):
        ProductId(value=product_id)


def test_company_id_hash():
    company_id = CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    assert hash(company_id) == hash(
        "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
    )


def test_company_id_hash_multiple():
    company_id1 = CompanyId(
        "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
    )
    company_id2 = CompanyId(
        "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
    )
    company_id3 = CompanyId(
        "urn:pathfinder:company:customcode:buyer-assigned:other-corp"
    )

    assert hash(company_id1) == hash(company_id2)
    assert hash(company_id1) != hash(company_id3)
