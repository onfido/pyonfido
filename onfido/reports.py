from .api_resource import ApiResource
from .defaults import * # flake8: noqa

class ReportType(object):
    IdentityReport = "identity"
    DocumentReport = "document"
    EmploymentReport = "employment"
    EducationReport = "education"
    NegativeMediaReport = "negative_media"
    DirectorshipReport = "directorship"
    CriminalRecordReport = "criminal_history"
    PEPSanctionReport = "watchlist"
    AntiMoneyLaunderingReport = "anti_money_laundering"
    StreetLevelReport = "street_level"
    SexOffenderReport = "sex_offender"
    WatchlistReport = "watchlist"
    NationalCriminalReport = "national_criminal"
    EvictionReport = "eviction"
    CountyCriminalReport = "county_criminal"
    DrivingRecord = "Report driving_record"


class Reports(ApiResource):
    def find(self, check_id, report_id):
        return self.get("checks/{0}/reports/{1}".format(check_id, report_id))

    def all(self, check_id):

        return self.get("checks/{0}/reports".format(check_id))
