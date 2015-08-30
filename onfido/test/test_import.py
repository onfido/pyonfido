import unittest2

# simplest and first test, can we import the onfido module

class ImportTests(unittest2.TestCase):

    def test_import(self):
        import onfido # flake8: noqa

    def test_from_import(self):
        from onfido import Api # flake8: noqa
