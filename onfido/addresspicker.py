from resources import ApiResource


class AddressPicker(ApiResource):
    def all(self, postcode):
        params = {
            "postcode": postcode
        }

        return self.get("applicants/addresses/pick", params)
