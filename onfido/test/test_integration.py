from onfido import Api
from .test_data import * # flake8: noqa
import unittest2
import os
import time
import random

class IntegrationTest(unittest2.TestCase):

    def create_api(self):
        # suitable obtuse enough env variable that it won't be set already
        api_token = os.environ['ONFIDO_INTEGRATION_TEST_API_TOKEN']
        return Api(api_token)


    def create_input_applicant(self):
        timestamp = str(int(time.time()))

        input_applicant = test_applicant
        input_applicant["last_name"] = timestamp
        input_applicant["email"] = "{0}@example.com".format(timestamp)

        return input_applicant

    def test_integration_applicant(self):
        api = self.create_api()
        input_applicant = self.create_input_applicant()
        created_applicant = api.Applicants.create(input_applicant)

        onfido_created_fields = [ "id", "href", "created_at" ]
        for onfido_field in onfido_created_fields:
            self.assertTrue(onfido_field in created_applicant)

        for input_field in input_applicant.keys():
            self.assertTrue(input_field in created_applicant)

        retrieved_applicant = api.Applicants.find(created_applicant["id"])

        for field in retrieved_applicant.keys():
            self.assertEqual(retrieved_applicant[field],
                             created_applicant[field])

        all_applicants = api.Applicants.all()

        found_applicant = False
        for applicant in all_applicants["applicants"]:
            if applicant["id"] == created_applicant["id"]:
                found_applicant = True

        self.assertTrue(found_applicant)

    def test_integration_document(self):
        api = self.create_api()
        applicant = random.choice(api.Applicants.all()["applicants"])
        document = open("onfido/test/passport.png", "rb")
        doc_response = api.Documents.create(applicant["id"], document, "passport.png", "passport")

        self.assertIn("id", doc_response)

    def test_integration_live_photo(self):
        api = self.create_api()
        applicant = api.Applicants.all()["applicants"][0]
        live_photo = open("onfido/test/passport.png", "rb")
        response = api.LivePhotos.create(applicant["id"], live_photo,
                                         'passport.png')

        self.assertIn("id", response)

    def test_integration_check(self):
        api = self.create_api()
        input_applicant = self.create_input_applicant()
        created_applicant = api.Applicants.create(input_applicant)

        check_details = {
            "type": 'standard',
            "reports": [{ "name": 'identity' }]
        }

        created_check = api.Checks.create(created_applicant["id"], check_details)
        self.assertIn("id", created_check)

        retrieved_check = api.Checks.find(created_applicant["id"], created_check["id"])

        for field in retrieved_check.keys():
            if field not in [ "reports" ]: # different value returned when creating vs returning :-S
                self.assertEqual(retrieved_check[field],
                                 created_check[field])

        all_checks = api.Checks.all(created_applicant["id"])
        found_check = False
        for check in all_checks["checks"]:
            if check["id"] == created_check["id"]:
                found_check = True

        self.assertTrue(found_check)

    def test_integration_report(self):
        # setup a new applicant + check
        api = self.create_api()
        input_applicant = self.create_input_applicant()
        created_applicant = api.Applicants.create(input_applicant)

        check_details = {
            "type": 'standard',
            "reports": [{ "name": 'identity' }]
        }

        created_check = api.Checks.create(created_applicant["id"], check_details)

        report_id = created_check["reports"][0]["id"]

        report = api.Reports.find(created_check["id"], report_id)

        self.assertIn("id", report)

        all_reports = api.Reports.all(created_check["id"])
        report_found = False
        for report in all_reports["reports"]:
            if report["id"] == report_id:
                report_found = True

        self.assertTrue(report_found)
