import json
import requests
from .defaults import * # flake8: noqa


class OnfidoApiRequestor(object):

    def __init__(self, api_key, version):
        self.api_key = api_key
        self.onfido_url = default_onfido_url + version + '/'

    def build_url(self, path):
        return self.onfido_url + path

    def headers(self, including_file=False):
        headers = {
            "Authorization": "Token token={0}".format(self.api_key)
        }

        if not including_file:
            headers["Content-Type"] = "application/json"

        return headers

    def post(self, url, data, file=None):
        h = self.headers(file is not None)
        response = requests.post(self.build_url(url),
                                 data=data,
                                 headers=h,
                                 files=file)
        return json.loads(response.text)

    def get(self, url, params):
        response = requests.get(self.build_url(url),
                                params=params,
                                headers=self.headers())
        return json.loads(response.text)
