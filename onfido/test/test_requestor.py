import json
import requests_mock
import unittest2
from onfido import Api
from .test_data import * # flake8: noqa

# test the requestor that communicates with Onfido directly
# need to flesh this out more, we're at 99% coverage but that means nothing
# if we're firing garbage at them.

def MockResponse(method):
    return json.dumps({
        "method": method
    })

class RequestorTests(unittest2.TestCase):

    def setup_mocks(self, mock_api):
        mock_api.post("https://api.onfido.com/v2/applicants/{0}/documents/".format(test_applicant_id), text=MockResponse("post"))
        mock_api.post("https://api.onfido.com/v2/applicants", text=MockResponse("post"))
        mock_api.post("https://api.onfido.com/v2/live_photos", text=MockResponse("post"))
        mock_api.get("https://api.onfido.com/v2/applicants/{0}".format(test_applicant_id), text=MockResponse("get"))

    def test_post(self):
        with requests_mock.mock() as mock_api:
            self.setup_mocks(mock_api)
            api = Api(test_onfido_key)
            r = api.Applicants.create(test_applicant)
            self.assertEqual("post", r["method"])

    def test_post_with_file(self):
        with requests_mock.mock() as mock_api:
            self.setup_mocks(mock_api)
            api = Api(test_onfido_key)
            r = api.Documents.create(test_applicant_id, test_document, test_document_filename, test_document_type)
            self.assertEqual("post", r["method"])

    def test_post_with_simple_file(self):
        with requests_mock.mock() as mock_api:
            self.setup_mocks(mock_api)
            api = Api(test_onfido_key)
            r = api.LivePhotos.create(test_applicant_id, test_photo,
                                      test_photo_filename)
            self.assertEqual("post", r["method"])

    def test_get(self):
        with requests_mock.mock() as mock_api:
            self.setup_mocks(mock_api)
            api = Api(test_onfido_key)
            r = api.Applicants.find(test_applicant_id)
            self.assertEqual("get", r["method"])
