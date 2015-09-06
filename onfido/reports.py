import defaults
from resources import ApiResource


class Reports(ApiResource):
    def find(self, check_id, report_id):
        return self.get("checks/{0}/reports/{1}".format(check_id, report_id))

    def all(self, check_id, page=defaults.page, per_page=defaults.per_page):

        params = {
            "page": page,
            "per_page": per_page
        }

        return self.get("checks/{0}/reports".format(check_id), params)
