from pathfinder_framework.urn import ProductId


class ProductIdList:
    def __init__(self, product_ids):
        if not isinstance(product_ids, list) or not all(isinstance(product_id, ProductId) for product_id in product_ids):
            raise ValueError("product_ids must be a list of ProductId")
        if len(set(product_ids)) != len(product_ids):
            raise ValueError("Duplicate product_ids are not allowed")
        self.product_ids = product_ids

    def __iter__(self):
        return iter(self.product_ids)

    def __len__(self):
        return len(self.product_ids)

    def __getitem__(self, index):
        return self.product_ids[index]

    def __setitem__(self, index, value):
        if not isinstance(value, ProductId):
            raise ValueError("product_id must be an instance of ProductId")
        self.product_ids[index] = value

    def __delitem__(self, index):
        del self.product_ids[index]

    def append(self, product_id):
        if not isinstance(product_id, ProductId):
            raise ValueError("product_id must be an instance of ProductId")
        if product_id in self.product_ids:
            raise ValueError("Duplicate product_ids are not allowed")
        self.product_ids.append(product_id)

    def insert(self, index, product_id):
        if not isinstance(product_id, ProductId):
            raise ValueError("product_id must be an instance of ProductId")
        if product_id in self.product_ids:
            raise ValueError("Duplicate product_ids are not allowed")
        self.product_ids.insert(index, product_id)

    def remove(self, product_id):
        if product_id not in self.product_ids:
            raise ValueError("product_id is not in the list")
        self.product_ids.remove(product_id)
