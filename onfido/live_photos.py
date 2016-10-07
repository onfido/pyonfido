"""Wrapper for the live photos endpoint."""
import mimetypes

from. api_resource import ApiResource


class LivePhotos(ApiResource):
    """Represents the Live Photos API endpoint."""
    def create(self, applicant_id, live_photo):
        """POST to /live_photos

        Args:
            applicant_id: ID of the applicant this photo belongs to (str).
            live_photo: The live photo to upload (file-like object).
        """
        filename = live_photo.name
        content_type = mimetypes.guess_type(filename)
        file = {'file': (filename, live_photo, content_type[0])}
        data = {'applicant_id': applicant_id}
        return self.post('live_photos', data, file)
