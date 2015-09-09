# pyonfido [![Build Status](https://travis-ci.org/smcl/pyonfido.svg?branch=master)](https://travis-ci.org/smcl/pyonfido) [![Coverage Status](https://coveralls.io/repos/smcl/pyonfido/badge.svg?branch=master&service=github)](https://coveralls.io/github/smcl/pyonfido?branch=master)

Pyonfido is a python API client for Onfido's REST API.

# Installation

You can either obtain pyonfido from PyPi (NOTE: IN PROGRESS, WILL NOT WORK):

    $ pip install pyonfido

Or just retrieve from source and install using the provided setup.py

    $ git clone https://github.com/stripe/stripe-python.git
    $ cd pyonfido
    $ python setup.py install

# Usage

Import the onfido.Api class, and create a new instance of it passing your api token as a parameter to the constructor:
    
    from onfido import Api

    # ...

    api = new Api("live_yV85IsmuYwmjQGlZ-4cNqdLSqOLbCtKA")

## Applicants

The [applicant](https://onfido.com/documentation#applicants) endpoint supports three operations - create(), find(), and all():

### Create applicant

    applicant_details = {
    	"title": "Mr",
    	"first_name": "John",
    	"last_name": "Smith"
    	# ...
    }

    applicant = api.Applicants.create(applicant_details)

### Retrieve applicant

    applicant_id = "1030303-123123-123123"	

    applicant = api.Applicants.find(applicant_id)

### List applicants    

    applicants = api.Applicants.all()

The all() operation also permits pagination

    top10_applicants = api.Applicants.all(1, 10):
    next10_applicants = api.Applicants.all(2, 10):

or

    top10_applicants = api.Applicants.all(page=1, per_page=10):
    next10_applicants = api.Applicants.all(page=2, per_page=10):

## Documents

### Upload document

	applicant_id = "1030303-123123-123123"

	document_file = open("passport.png", "rb")

	document = api.Documents.create(applicant_id, document_file, "passport.png", "passport")

You can use any file-like object in place of the document_file parameter, so you needn't save to disk and call open() if you have the file in, say, an BytesIO object in memory.

## Checks

### Create check

	applicant_id = "1030303-123123-123123"

    check_args = {
        type: 'standard',
        reports: [{ name: 'identity' }]
    }

    check = api.Checks.create(applicant_id, create_args)

### Retrieve check

    applicant_id = "1030303-123123-123123"

    check_id = "8546921-123123-123123"

    check = api.Checks.find(applicant_id, check_id)

### List checks

    applicant_id = "1030303-123123-123123"
    
    checks = api.Checks.all(applicant_id)

Pagination is supported through the page and per_page parameters:

    top10_checks = api.Checks.all(applicant_id, 1, 10):
    next_checks = api.Checks.all(applicant_id, 2, 10):

or

    top10_checks = api.Checks.all(applicant_id, page=1, per_page=10):
    next10_checks = api.Checks.all(applicant_id, page=2, per_page=10):

## Reports

### Retrieve report

	check_id = "8546921-123123-123123"

	report_id = "1256879-123123-456789"

	report = api.Reports.find(check_id, report_id)

### List reports

    check_id = "8546921-123123-123123"

    reports = api.Reports.all(check_id)

# Running tests

To confirm that things are working as expected you can run the unit tests using {{setup.py}} or checking the [CI](https://travis-ci.org/smcl/pyonfido)

    $ python setup.py test

The code should also be compliant with [PEP-8](https://www.python.org/dev/peps/pep-0008/), which you can confirm by installing and running flake8 on the onfido library:

	$ pip install flake8
    $ flake8 onfido

There are also a handful of integration tests which connect to the Onfido API, they will only be run if you set the {{ONFIDO_INTEGRATION_TEST_API_TOKEN}} environment variable and run the tests:

    $ ONFIDO_INTEGRATION_TEST_API_TOKEN=my_test_api_key python setup.py test

The environment variable was deliberately chosen to be long and obtuse to lessen the chances that it's already set, but you should exercise caution anyway as this will result in creating a number of new applicants and checks.

# TODO
* finalise submission of library into pypi
* improve this README
* support constants better (DocumentType etc)
