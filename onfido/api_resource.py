import json


class ApiResource(object):
    def __init__(self, requestor):
        self.requestor = requestor

    def post(self, url, data, file=None):
        if file:
            return self.requestor.post(url, data, file=file)
        return self.requestor.post(url, json.dumps(data))

    def get(self, url, params=None):
        return self.requestor.get(url, params)
