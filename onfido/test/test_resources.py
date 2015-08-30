import unittest2

from onfido import Api

under_test_applicant_id = "1030303-123123-123123"

under_test_applicant = {
    "title": "Mr",
    "first_name": "John",
    "last_name": "Smith",
    "gender": "male",
    "dob": "2013-02-17",
    "telephone": "02088909293",
    "country": "GBR",
    "addresses": [
        {
            "building_number": "100",
            "street": "Main Street",
            "town": "London",
            "postcode": "SW4 6EH",
            "country": "GBR",
            "start_date": "2013-08-10"
        }
    ]
}

under_test_page_no = 2

under_test_per_page = 20

under_test_document = {
    "type": "passport",
    "file": None # bytes([50, 19, 100])  # some nonsense
}

under_test_check_id = "8546921-123123-123123"

under_test_check = {
    "type": 'standard',
    "reports": [
        {
            "name": "criminal_history",
            "redirect_uri": "https://www.onfido.com",
            "variant": "enhanced",
            "options": [
                {
                    "name": "children_barred_list",
                    "options": [
                        {
                            "name": "speedy"
                        }
                    ]
                }
            ]
        }
    ]
}

under_test_report_id = "1256879-123123-456789"

under_test_postcode = "SW4 6EH"


class DummyApiRequestor(object):
    def post(self, url, params):
        return {
            "url": url,
            "params": params,
            "method": "post"
        }

    def get(self, url, params):
        return {
            "url": url,
            "params": params,
            "method": "get"
        }


class ResourceTestCase(unittest2.TestCase):
    def setup(self):
        self.api = Api("", DummyApiRequestor())


#  verify the interface to the API is as-expected, so just fire through
#  some very simple data and so long as python doesn't barf we're all good.

class InterfaceTests(ResourceTestCase):
    def test_applicants_interface(self):
        self.setup()
        self.api.Applicants.create(under_test_applicant)
        self.api.Applicants.find(under_test_applicant_id)
        self.api.Applicants.all()
        self.api.Applicants.all(page=under_test_page_no,
                                per_page=under_test_per_page)

    def test_documents_interface(self):
        self.setup()
        self.api.Documents.create(under_test_applicant_id,
                                  under_test_document)

    def test_checks_interface(self):
        self.setup()
        self.api.Checks.create(under_test_applicant_id, under_test_check)
        self.api.Checks.find(under_test_applicant_id, under_test_check_id)
        self.api.Checks.all(under_test_applicant_id)
        self.api.Checks.all(under_test_applicant_id,
                            page=under_test_page_no,
                            per_page=under_test_per_page)

    def test_reports_interface(self):
        self.setup()
        self.api.Reports.find(under_test_check_id, under_test_report_id)
        self.api.Reports.all(under_test_check_id)

    def test_addresspicker_interface(self):
        self.setup()
        self.api.AddressPicker.all(under_test_postcode)


#  check we generate the appropriate path part of request url
#  and use the correct http method
class ResourcePathAndMethodTests(ResourceTestCase):
    def test_applicants_create_path_method(self):
        self.setup()
        result = self.api.Applicants.create(under_test_applicant)
        self.assertEqual("applicants", result["url"])
        self.assertEqual("post", result["method"])

    def test_applicants_find_path_method(self):
        self.setup()
        result = self.api.Applicants.find(under_test_applicant_id)
        self.assertEqual("applicants/{0}".format(under_test_applicant_id),
                         result["url"])
        self.assertEqual("get", result["method"])

    def test_applicants_list_path_method(self):
        self.setup()
        result = self.api.Applicants.all()
        self.assertEqual("applicants", result["url"])
        self.assertEqual("get", result["method"])

    def test_applicant_list_paginate_path_method(self):
        self.setup()
        result = self.api.Applicants.all(page=under_test_page_no,
                                         per_page=under_test_per_page)
        self.assertEqual("applicants", result["url"])
        self.assertEqual("get", result["method"])
        self.assertEqual(under_test_page_no, result["params"]["page"])
        self.assertEqual(under_test_per_page, result["params"]["per_page"])

    def test_documents_path_method(self):
        self.setup()
        result = self.api.Documents.create(under_test_applicant_id,
                                           under_test_document)
        self.assertEqual(
            "applicants/{0}/documents/".format(under_test_applicant_id),
            result["url"])
        self.assertEqual("post", result["method"])

    def test_checks_create_path_method(self):
        self.setup()
        result = self.api.Checks.create(under_test_applicant_id,
                                        under_test_check)
        self.assertEqual(
            "applicants/{0}/checks".format(under_test_applicant_id),
            result["url"])
        self.assertEqual("post", result["method"])

    def test_checks_find_path_method(self):
        self.setup()
        result = self.api.Checks.find(under_test_applicant_id,
                                      under_test_check_id)
        self.assertEqual(
            "applicants/{0}/checks/{1}".format(under_test_applicant_id,
                                               under_test_check_id),
            result["url"])
        self.assertEqual("get", result["method"])

    def test_checks_list_path_method(self):
        self.setup()
        result = self.api.Checks.all(under_test_applicant_id)
        self.assertEqual(
            "applicants/{0}/checks".format(under_test_applicant_id),
            result["url"])
        self.assertEqual("get", result["method"])

    def test_checks_list_paginate_path_method(self):
        self.setup()
        result = self.api.Checks.all(under_test_applicant_id,
                                     page=under_test_page_no,
                                     per_page=under_test_per_page)
        self.assertEqual(
            "applicants/{0}/checks".format(under_test_applicant_id),
            result["url"])
        self.assertEqual(under_test_page_no, result["params"]["page"])
        self.assertEqual(under_test_per_page, result["params"]["per_page"])
        self.assertEqual("get", result["method"])

    def test_reports_find_path_method(self):
        self.setup()
        result = self.api.Reports.find(under_test_check_id,
                                       under_test_report_id)
        self.assertEqual(
            "checks/{0}/reports/{1}".format(under_test_check_id,
                                            under_test_report_id),
            result["url"])
        self.assertEqual("get", result["method"])

    def test_reports_list_path_method(self):
        self.setup()
        result = self.api.Reports.all(under_test_check_id)
        self.assertEqual("checks/{0}/reports".format(under_test_check_id),
                         result["url"])
        self.assertEqual("get", result["method"])

    def test_address_list_path_method(self):
        self.setup()
        result = self.api.AddressPicker.all(under_test_postcode)
        self.assertEqual("applicants/addresses/pick", result["url"])
        self.assertEqual("get", result["method"])
