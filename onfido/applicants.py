import defaults
from resources import ApiResource


class Applicants(ApiResource):
    def create(self, applicant_details):
        return self.post("applicants", applicant_details)

    def find(self, applicant_id):
        return self.get("applicants/{0}".format(applicant_id))

    def all(self, page=defaults.page, per_page=defaults.per_page):
        params = {
            "page": page,
            "per_page": per_page
        }

        return self.get("applicants", params)
