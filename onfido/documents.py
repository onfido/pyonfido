import mimetypes
import os
from .api_resource import ApiResource


class DocumentType():
    Passport = "passport"
    NationalIdentityCard = "national_identity_card"
    WorkPermit = "work_permit"
    DrivingLicense = "driving_licence"
    NationalInsurance = "national_insurance"
    BirthCertificate = "birth_certificate"
    BankStatement = "bank_statement"
    Unknown = "unknown"


class Documents(ApiResource):
    def create(self, applicant_id, document, document_filename, doc_type):
        mimetypes.init()

        filename, extension = os.path.splitext(document_filename)

        data = {
            "type": doc_type
        }

        files = {
            "file": (document_filename, document,
                     mimetypes.types_map[extension])
        }

        return self.post("applicants/{0}/documents/".format(applicant_id),
                         data,
                         files)
