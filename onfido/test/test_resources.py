import unittest2
from .test_data import * # flake8: noqa
from onfido import Api


class DummyApiRequestor(object):
    def post(self, url, params, file=None):
        return {
            "url": url,
            "params": params,
            "method": "post",
            "file": file
        }

    def get(self, url, params):
        return {
            "url": url,
            "params": params,
            "method": "get"
        }


class ResourceTestCase(unittest2.TestCase):
    def setup(self):
        self.api = Api("", 'v2', DummyApiRequestor())


#  verify the interface to the API is as-expected, so just fire through
#  some very simple data and so long as python doesn't barf we're all good.

class InterfaceTests(ResourceTestCase):
    def test_applicants_interface(self):
        self.setup()
        self.api.Applicants.create(test_applicant)
        self.api.Applicants.find(test_applicant_id)
        self.api.Applicants.all()
        self.api.Applicants.all(page=test_page_no,
                                per_page=test_per_page)

    def test_documents_interface(self):
        self.setup()
        self.api.Documents.create(test_applicant_id, test_document, test_document_filename, test_document_type)

    def test_live_photos_interface(self):
        self.setup()
        self.api.LivePhotos.create(test_applicant_id, test_photo,
                                   test_photo_filename)

    def test_checks_interface(self):
        self.setup()
        self.api.Checks.create(test_applicant_id, test_check)
        self.api.Checks.find(test_applicant_id, test_check_id)
        self.api.Checks.all(test_applicant_id)
        self.api.Checks.all(test_applicant_id,
                            page=test_page_no,
                            per_page=test_per_page)

    def test_reports_interface(self):
        self.setup()
        self.api.Reports.find(test_check_id, test_report_id)
        self.api.Reports.all(test_check_id)

    def test_addresspicker_interface(self):
        self.setup()
        self.api.AddressPicker.all(test_postcode)


#  check we generate the appropriate path part of request url
#  and use the correct http method
class ResourcePathAndMethodTests(ResourceTestCase):
    def test_applicants_create_path_method(self):
        self.setup()
        result = self.api.Applicants.create(test_applicant)
        self.assertEqual("applicants", result["url"])
        self.assertEqual("post", result["method"])

    def test_applicants_find_path_method(self):
        self.setup()
        result = self.api.Applicants.find(test_applicant_id)
        self.assertEqual("applicants/{0}".format(test_applicant_id),
                         result["url"])
        self.assertEqual("get", result["method"])

    def test_applicants_list_path_method(self):
        self.setup()
        result = self.api.Applicants.all()
        self.assertEqual("applicants", result["url"])
        self.assertEqual("get", result["method"])

    def test_applicant_list_paginate_path_method(self):
        self.setup()
        result = self.api.Applicants.all(page=test_page_no,
                                         per_page=test_per_page)
        self.assertEqual("applicants", result["url"])
        self.assertEqual("get", result["method"])
        self.assertEqual(test_page_no, result["params"]["page"])
        self.assertEqual(test_per_page, result["params"]["per_page"])

    def test_documents_path_method(self):
        self.setup()
        result = self.api.Documents.create(test_applicant_id, test_document, test_document_filename, test_document_type)
        self.assertEqual(
            "applicants/{0}/documents/".format(test_applicant_id),
            result["url"])
        self.assertEqual("post", result["method"])

    def test_live_photos_path_method(self):
        self.setup()
        result = self.api.LivePhotos.create(test_applicant_id, test_photo,
                                            test_photo_filename)
        self.assertEqual("live_photos", result["url"])
        self.assertEqual("post", result["method"])

    def test_checks_create_path_method(self):
        self.setup()
        result = self.api.Checks.create(test_applicant_id,
                                        test_check)
        self.assertEqual(
            "applicants/{0}/checks".format(test_applicant_id),
            result["url"])
        self.assertEqual("post", result["method"])

    def test_checks_find_path_method(self):
        self.setup()
        result = self.api.Checks.find(test_applicant_id,
                                      test_check_id)
        self.assertEqual(
            "applicants/{0}/checks/{1}".format(test_applicant_id,
                                               test_check_id),
            result["url"])
        self.assertEqual("get", result["method"])

    def test_checks_list_path_method(self):
        self.setup()
        result = self.api.Checks.all(test_applicant_id)
        self.assertEqual(
            "applicants/{0}/checks".format(test_applicant_id),
            result["url"])
        self.assertEqual("get", result["method"])

    def test_checks_list_paginate_path_method(self):
        self.setup()
        result = self.api.Checks.all(test_applicant_id,
                                     page=test_page_no,
                                     per_page=test_per_page)
        self.assertEqual(
            "applicants/{0}/checks".format(test_applicant_id),
            result["url"])
        self.assertEqual(test_page_no, result["params"]["page"])
        self.assertEqual(test_per_page, result["params"]["per_page"])
        self.assertEqual("get", result["method"])

    def test_reports_find_path_method(self):
        self.setup()
        result = self.api.Reports.find(test_check_id,
                                       test_report_id)
        self.assertEqual(
            "checks/{0}/reports/{1}".format(test_check_id,
                                            test_report_id),
            result["url"])
        self.assertEqual("get", result["method"])

    def test_reports_list_path_method(self):
        self.setup()
        result = self.api.Reports.all(test_check_id)
        self.assertEqual("checks/{0}/reports".format(test_check_id),
                         result["url"])
        self.assertEqual("get", result["method"])

    def test_address_list_path_method(self):
        self.setup()
        result = self.api.AddressPicker.all(test_postcode)
        self.assertEqual("applicants/addresses/pick", result["url"])
        self.assertEqual("get", result["method"])
