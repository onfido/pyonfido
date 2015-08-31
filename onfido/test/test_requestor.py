import requests_mock
import unittest2
from onfido import Api
from .test_data import * # flake8: noqa


class RequestorTests(unittest2.TestCase):

    def setup_mocks(self, mock_api):
            mock_api.post('https://api.onfido.com/v1/applicants', text='post')
            mock_api.get('https://api.onfido.com/v1/applicants/{0}'.format(test_applicant_id), text='get')       

    def check_onfido_key(self, r):
        self.assertEqual("Token token={0}".format(test_onfido_key), r.request.headers["Authorization"])

    def test_post(self):
        with requests_mock.mock() as mock_api:
            self.setup_mocks(mock_api)
            api = Api(test_onfido_key)
            r = api.Applicants.create(test_applicant)
            self.assertEqual("post", r.text)
            self.check_onfido_key(r)

    def test_get(self):
        with requests_mock.mock() as mock_api:
            self.setup_mocks(mock_api)
            api = Api(test_onfido_key)
            r = api.Applicants.find(test_applicant_id)
            self.assertEqual("get", r.text)
            self.check_onfido_key(r)