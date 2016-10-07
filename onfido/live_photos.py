"""Wrapper for the live photos endpoint."""
from. api_resource import ApiResource


class LivePhotos(ApiResource):
    """Represents the Live Photos API endpoint."""
    def create(self, applicant_id, live_photo):
        """POST to /live_photos

        Args:
            applicant_id: ID of the applicant this photo belongs to (str).
            live_photo: The live photo to upload (file-like object).
        """
        data = {'applicant_id': applicant_id}
        file = {'file': live_photo}
        return self.post('live_photos', data, file)
