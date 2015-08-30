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

        self.Applicants = Applicants(requestor)
        self.Documents = Documents(requestor)
        self.Checks = Checks(requestor)
        self.Reports = Reports(requestor)
        self.AddressPicker = AddressPicker(requestor)
