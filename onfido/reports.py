from .api_resource import ApiResource
from .defaults import * # flake8: noqa


class Reports(ApiResource):
    def find(self, check_id, report_id):
        return self.get("checks/{0}/reports/{1}".format(check_id, report_id))

    def all(self, check_id):

        return self.get("checks/{0}/reports".format(check_id))
