import pkgutil
import unittest2
import os


def all_names():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        if modname.startswith('test_'):
            yield 'onfido.test.' + modname


def all():
    if "ONFIDO_INTEGRATION_TEST_API_TOKEN" in os.environ:
        return unittest2.defaultTestLoader.loadTestsFromNames(all_names())
    return unit()


def unit():
    unit_names = [name for name in all_names() if 'integration' not in name]
    return unittest2.defaultTestLoader.loadTestsFromNames(unit_names)
