from .requestor import OnfidoApiRequestor
from .applicants import Applicants  # flake8 : noqa
from .documents import Documents  # flake8 : noqa
from .checks import Checks  # flake8 : noqa
from .reports import Reports  # flake8 : noqa
from .addresspicker import AddressPicker  # flake8 : noqa


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
