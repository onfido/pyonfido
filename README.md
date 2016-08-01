# PyOnfido [![Build Status](https://travis-ci.org/onfido/pyonfido.svg?branch=master)](https://travis-ci.org/onfido/pyonfido) [![Coverage Status](https://coveralls.io/repos/onfido/pyonfido/badge.svg?branch=master&service=github)](https://coveralls.io/github/onfido/pyonfido?branch=master)

PyOnfido is a Python API client for Onfido's REST API. This package supports both v1 and v2 of the Onfido API.

# Installation

You can either obtain PyOnfido from PyPi:

    $ pip install pyonfido

Or just retrieve from source and install using the provided `setup.py`:

    $ git clone https://github.com/smcl/pyonfido.git
    $ cd pyonfido
    $ python setup.py install

# Usage

Import the `onfido.Api` class, and create a new instance of it passing your API token as a parameter to the constructor:

    from onfido import Api

    # ...

    api = Api("live_yV85IsmuYwmjQGlZ-4cNqdLSqOLbCtKA")

It is through this `api` object that you will interact with Onfido API.


To use v1 of the Onfido API :

    api = Api("live_yV85IsmuYwmjQGlZ-4cNqdLSqOLbCtKA", 'v1')

## Applicants

The [applicant](https://onfido.com/documentation#applicants) endpoint supports three operations - `create()`, `find()`, and `all()`:

#### Create applicant

    applicant_details = {
    	"title": "Mr",
    	"first_name": "John",
    	"last_name": "Smith"
    	# ...
    }

    applicant = api.Applicants.create(applicant_details)

#### Retrieve applicant

    applicant_id = "1030303-123123-123123"

    applicant = api.Applicants.find(applicant_id)

#### List applicants

    applicants = api.Applicants.all()

The `all()` operation also permits pagination

    top10_applicants = api.Applicants.all(1, 10):
    next10_applicants = api.Applicants.all(2, 10):

or

    top10_applicants = api.Applicants.all(page=1, per_page=10):
    next10_applicants = api.Applicants.all(page=2, per_page=10):

## Documents

The [documents](https://onfido.com/documentation#documents) endpoint supports one operation - `create()`:


#### Upload document

	applicant_id = "1030303-123123-123123"

	document_file = open("passport.png", "rb")

	document = api.Documents.create(applicant_id, document_file, "passport.png", "passport")

You can use any file-like object in place of the document_file parameter, so you needn't save to disk and call `open()` if you have the file in, say, an `BytesIO` object in memory.

#### Document types

The different document types supported by the onfido API are available by importing `DocumentType`:

    from onfido import DocumentType

    my_doc_type = DocumentType.Passport # "passport"
    my_doc_type = DocumentType.NationalIdentityCard # "national_identity_card"
    my_doc_type = DocumentType.WorkPermit # "work_permit"
    my_doc_type = DocumentType.DrivingLicense # "driving_license"
    my_doc_type = DocumentType.NationalInsurance # "national_insurance"
    my_doc_type = DocumentType.BirthCertificate # "birth_certificate"
    my_doc_type = DocumentType.BankStatement # "bank_statement"
    my_doc_type = DocumentType.Unknown # "unknown"

## Checks

The [checks](https://onfido.com/documentation#checks) endpoint supports three operations - `create()`, `find()` and `all()`:

#### Create check

	applicant_id = "1030303-123123-123123"

    check_args = {
        "type": "standard",
        "reports": [{ "name": "identity" }]
    }

    check = api.Checks.create(applicant_id, check_args)

#### Retrieve check

    applicant_id = "1030303-123123-123123"

    check_id = "8546921-123123-123123"

    check = api.Checks.find(applicant_id, check_id)

#### List checks

    applicant_id = "1030303-123123-123123"

    checks = api.Checks.all(applicant_id)

Pagination is supported through the page and per_page parameters:

    top10_checks = api.Checks.all(applicant_id, 1, 10):
    next_checks = api.Checks.all(applicant_id, 2, 10):

or

    top10_checks = api.Checks.all(applicant_id, page=1, per_page=10):
    next10_checks = api.Checks.all(applicant_id, page=2, per_page=10):

## Reports

The [reports](https://onfido.com/documentation#reports) endpoint supports two operations - `find()` and `all()`:

#### Retrieve report

	check_id = "8546921-123123-123123"

	report_id = "1256879-123123-456789"

	report = api.Reports.find(check_id, report_id)

#### List reports

    check_id = "8546921-123123-123123"

    reports = api.Reports.all(check_id)

#### Report types

The different document types supported by the onfido API are available by importing `ReportType`:

    from onfido import ReportType

    my_report_type = ReportType.IdentityReport # "identity"
    my_report_type = ReportType.DocumentReport # "document"
    my_report_type = ReportType.EmploymentReport # "employment"
    my_report_type = ReportType.EducationReport # "education"
    my_report_type = ReportType.NegativeMediaReport # "negative_media"
    my_report_type = ReportType.DirectorshipReport # "directorship"
    my_report_type = ReportType.CriminalRecordReport # "criminal_history"
    my_report_type = ReportType.PEPSanctionReport # "watchlist"
    my_report_type = ReportType.AntiMoneyLaunderingReport # "anti_money_laundering"
    my_report_type = ReportType.StreetLevelReport # "street_level"
    my_report_type = ReportType.SexOffenderReport # "sex_offender"
    my_report_type = ReportType.WatchlistReport # "watchlist"
    my_report_type = ReportType.NationalCriminalReport # "national_criminal"
    my_report_type = ReportType.EvictionReport # "eviction"
    my_report_type = ReportType.CountyCriminalReport # "county_criminal"
    my_report_type = ReportType.DrivingRecordReport # "driving_record"

# Running tests

To confirm that things are working as expected you can check the [CI](https://travis-ci.org/smcl/pyonfido) or run the unit tests using `setup.py`:

    $ python setup.py test

The code should also be compliant with [PEP 8](https://www.python.org/dev/peps/pep-0008/), which you can confirm by installing and running flake8 on the onfido library:

    $ pip install flake8
    $ flake8 onfido

There are also a handful of integration tests which connect to the Onfido API, they will only be run if you set the `ONFIDO_INTEGRATION_TEST_API_TOKEN` environment variable and run the tests:

    $ ONFIDO_INTEGRATION_TEST_API_TOKEN=my_test_api_key python setup.py test

The environment variable was deliberately chosen to be long and obtuse to lessen the chances that it's already set, but you should exercise caution anyway as this will result in creating a number of new applicants and checks.
