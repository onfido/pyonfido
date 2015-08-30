import requests


class OnfidoApiRequestor(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.onfido_url = "https://api.onfido.com/v1/"

    def build_url(self, path):
        return self.onfido_url + path

    def headers(self):
        return {
            "Authorization": "Token token={0}".format(self.api_key),
            "Accept": "application/json"
        }

    def post(self, url, params):
        return requests.post(self.build_url(url),
                             params=params,
                             headers=self.headers())

    def get(self, url, params):
        return requests.get(self.build_url(url),
                            params=params,
                            headers=self.headers())
