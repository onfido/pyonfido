import os
from setuptools import setup

setup(
    name = "PyOnfido",
    version = "0.5",
    author = "Onfido",
    author_email = "engineering@onfido.com",
    description = ("Python wrapper library for Onfido's REST API for background checking."),
    license = "BSD",
    keywords = "pyonfido onfido background",
    url = "https://github.com/onfido/pyonfido",
    download_url = 'https://github.com/onfido/pyonfido/tarball/0.5',
    packages=['onfido', 'onfido.test'],
    test_suite='onfido.test.all',
    classifiers=[
        "Development Status :: 5 - Production/Stable ",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=[
        'requests',
        'requests_mock',
        'unittest2'
    ],
    setup_requires=[
        'requests',
        'requests_mock',
        'unittest2'
    ],
)
