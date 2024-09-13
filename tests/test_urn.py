import pytest

from pact_methodology.urn import URN, CompanyId, ProductId


def test_valid_urn():
    urn_string = "urn:isbn:978-0-596-52932-1"
    urn = URN(value=urn_string)
    assert urn.value == urn_string


def test_invalid_urn_format():
    with pytest.raises(ValueError):
        URN(value="not-a-valid-urn")


def test_isbn_urn():
    urn = URN(value="urn:isbn:978-0-596-52932-1")
    assert urn.value == "urn:isbn:978-0-596-52932-1"


def test_uuid_urn():
    urn = URN(value="urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
    assert urn.value == "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6"


@pytest.mark.parametrize(
    "urn_string",
    [
        "urn:pathfinder:company:customcode:buyer-assigned:4321",
        "urn:pathfinder:company:customcode:vendor-assigned:6789",
        "urn:pathfinder:product:customcode:buyer-assigned:1234",
        "urn:pathfinder:product:customcode:vendor-assigned:8765",
        "urn:pathfinder:product:id:cas:64-17-5",
        "urn:pathfinder:product:id:iupac-inchi:1S%2FC9H8O4%2Fc1-6%2810%2913-8-5-3-2-4-7%288%299%2811%2912%2Fh2-5H%2C1H3%2C%28H%2C11%2C12%29",
    ],
)
def test_valid_pathfinder_urns(urn_string):
    urn = URN(value=urn_string)
    assert urn.value == urn_string


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
