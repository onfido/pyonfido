import os
from setuptools import setup

setup(
    name = "PyOnfido",
    version = "0.0.1",
    author = "Sean McLemon",
    author_email = "sean.mclemon@gmail.com",
    description = ("Python wrapper library for Onfido's background checking REST API."),
    license = "BSD",
    keywords = "onfido background",
    url = "https://github.com/smcl/pyonfido",
    packages=['onfido', 'onfido.test'],
    test_suite='onfido.test.all',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ],
    install_requires=[
        'requests',
        'requests_mock',
        'unittest2'
    ],
)