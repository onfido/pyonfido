from .api_resource import ApiResource
from .defaults import * # flake8: noqa


class Reports(ApiResource):
    def find(self, check_id, report_id):
        return self.get("checks/{0}/reports/{1}".format(check_id, report_id))

    def all(self, check_id, page=default_page, per_page=default_per_page):

        params = {
            "page": page,
            "per_page": per_page
        }

        return self.get("checks/{0}/reports".format(check_id), params)
