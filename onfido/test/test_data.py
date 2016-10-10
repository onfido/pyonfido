import io

# the test data below was mostly taken from https://onfido.com/documentation
test_onfido_key = "live_yV85IsmuYwmjQGlZ-4cNqdLSqOLbCtKA"

test_applicant_id = "1030303-123123-123123"

test_applicant = {
    "title": "Mr",
    "first_name": "John",
    "last_name": "Smith",
    "gender": "male",
    "dob": "2013-02-17",
    "telephone": "02088909293",
    "country": "GBR",
    "addresses": [
        {
            "building_number": "100",
            "street": "Main Street",
            "town": "London",
            "postcode": "SW4 6EH",
            "country": "GBR",
            "start_date": "2013-08-10"
        }
    ],
    "email": "test@example.com"
}

test_page_no = 2

test_per_page = 20

test_photo = io.BytesIO(b"some photo text \x02\x01\x00")

test_photo_filename = "test.jpg"

test_document = io.BytesIO(b"some document text \x00\x01\x02")

test_document_filename = "test.bmp"

test_document_type = "passport"

test_check_id = "8546921-123123-123123"

test_check = {
    "type": 'standard',
    "reports": [
        {
            "name": "criminal_history",
            "redirect_uri": "https://www.onfido.com",
            "variant": "enhanced",
            "options": [
                {
                    "name": "children_barred_list",
                    "options": [
                        {
                            "name": "speedy"
                        }
                    ]
                }
            ]
        }
    ]
}

test_report_id = "1256879-123123-456789"

test_postcode = "SW4 6EH"
