from .requestor import OnfidoApiRequestor
from .resources import (
    Applicants,
    Documents,
    Checks,
    Reports,
    AddressPicker
)


class Api(object):
    def __init__(self, api_key, requestor=None):

        if not requestor:
            self.requestor = OnfidoApiRequestor(api_key)
        else:
            self.requestor = requestor

        self.Applicants = Applicants(self.requestor)
        self.Documents = Documents(self.requestor)
        self.Checks = Checks(self.requestor)
        self.Reports = Reports(self.requestor)
        self.AddressPicker = AddressPicker(self.requestor)
