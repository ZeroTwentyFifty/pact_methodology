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
    "company_id, error_message",
    [
        ("urn:pathfinder:company:customcode:vendor-assigned:", "CompanyId does not conform to the required format"),
        ("urn:pathfinder:company:customcode:invalid-type:12345", "CompanyId does not conform to the required format"),
        ("urn:pathfinder:company:customcode:buyer-assigned:", "CompanyId does not conform to the required format"),
        ("not-a-valid-urn", "Value must be a valid URN"),
        ("urn:invalid", "Value must be a valid URN"),
    ],
)
def test_invalid_company_ids(company_id, error_message):
    """Test initialization with invalid CompanyId strings."""
    with pytest.raises(ValueError, match=error_message):
        CompanyId(value=company_id)


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


@pytest.mark.parametrize(
    "urn_string",
    [
        "urn:pathfinder:product:customcode:buyer-assigned:acme-product",
        "urn:pathfinder:product:customcode:vendor-assigned:12345",
        "urn:pathfinder:product:id:cas:64-17-5",
        "urn:pathfinder:product:id:cas:1067-08-9",
        "urn:pathfinder:product:id:cas:2306877-20-1",
        "urn:pathfinder:product:id:iupac-inchi:1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)",
    ],
)
def test_valid_product_id(urn_string):
    """Test initialization with valid ProductId strings."""
    product_id = ProductId(value=urn_string)
    assert product_id.value == urn_string


@pytest.mark.parametrize(
    "urn_string, error_message",
    [
        ("not-a-valid-urn", "Value must be a valid URN"),
        ("urn:invalid", "Value must be a valid URN"),
        ("urn:pathfinder:product:customcode:invalid:ABC-123", "ProductId does not conform to the required format"),
        ("urn:pathfinder:product:id:cas:12345-67-9", "ProductId does not conform to the required format"),  # Invalid CAS number
    ],
)
def test_invalid_product_id(urn_string, error_message):
    """Test initialization with invalid ProductId strings."""
    with pytest.raises(ValueError, match=error_message):
        ProductId(value=urn_string)


def test_str_representation():
    """Test string representation of ProductId."""
    urn_string = "urn:pathfinder:product:customcode:buyer-assigned:ABC-123"
    product_id = ProductId(value=urn_string)
    assert str(product_id) == urn_string


def test_repr_representation():
    """Test representation of ProductId."""
    urn_string = "urn:pathfinder:product:customcode:buyer-assigned:ABC-123"
    product_id = ProductId(value=urn_string)
    assert repr(product_id) == f"ProductId(value='{urn_string}')"


def test_hash():
    """Test hash functionality of ProductId."""
    urn_string = "urn:pathfinder:product:customcode:buyer-assigned:ABC-123"
    product_id = ProductId(value=urn_string)
    assert hash(product_id) == hash(urn_string)


def test_equality_same_instance():
    """Test equality of the same ProductId instance."""
    product_id = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    assert product_id == product_id


def test_equality_different_instances():
    """Test equality of different ProductId instances with the same value."""
    product_id1 = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    product_id2 = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    assert product_id1 == product_id2


def test_inequality_different_values():
    """Test inequality of ProductId instances with different values."""
    product_id1 = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    product_id2 = ProductId(value="urn:pathfinder:product:customcode:vendor-assigned:XYZ-456")
    assert product_id1 != product_id2


def test_inequality_with_non_product_id():
    """Test inequality of ProductId instance with non-ProductId object."""
    product_id = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    assert product_id != "urn:pathfinder:product:customcode:buyer-assigned:ABC-123"
    assert product_id != 123
    assert product_id != None


def test_hash_consistency():
    """Test hash consistency across different instances with the same value."""
    product_id1 = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    product_id2 = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    assert hash(product_id1) == hash(product_id2)


def test_hash_inequality():
    """Test hash inequality for different ProductId values."""
    product_id1 = ProductId(value="urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
    product_id2 = ProductId(value="urn:pathfinder:product:customcode:vendor-assigned:XYZ-456")
    assert hash(product_id1) != hash(product_id2)
