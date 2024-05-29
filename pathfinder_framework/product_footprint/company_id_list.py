from pathfinder_framework.urn import CompanyId


class CompanyIdList:
    def __init__(self, company_ids):
        if not isinstance(company_ids, list) or not all(isinstance(company_id, CompanyId) for company_id in company_ids):
            raise ValueError("company_ids must be a list of CompanyId")
        if len(set(company_ids)) != len(company_ids):
            raise ValueError("Duplicate company_ids are not allowed")
        self.company_ids = company_ids

    def __iter__(self):
        return iter(self.company_ids)

    def __len__(self):
        return len(self.company_ids)

    def __getitem__(self, index):
        return self.company_ids[index]
