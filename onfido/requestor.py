import json
import requests

default_onfido_url = "https://api.onfido.com/v1/"


class OnfidoApiRequestor(object):

    def __init__(self, api_key, onfido_url=default_onfido_url):
        self.api_key = api_key
        self.onfido_url = onfido_url

    def build_url(self, path):
        return self.onfido_url + path

    def headers(self):
        return {
            "Authorization": "Token token={0}".format(self.api_key),
            "Content-Type": "application/json"
        }

    def post(self, url, data):
        return requests.post(self.build_url(url),
                             data=json.dumps(data),
                             headers=self.headers())

    def get(self, url, params):
        return requests.get(self.build_url(url),
                            params=params,
                            headers=self.headers())
