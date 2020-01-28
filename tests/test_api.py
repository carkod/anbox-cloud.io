import unittest
from webapp.app import app, _api_request
from werkzeug.exceptions import HTTPException


class TestApi(unittest.TestCase):
    def setUp(self):
        """
        Set up Flask app for testing
        """
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_api_requests_200(self):

        response = _api_request(
            "1.0/token",
            params={"provider": "usso"}
        )
        self.assertEqual(response["status_code"], 200)

    def test_api_requests_401(self):
        response = _api_request("1.0/instances")
        self.assertEqual(response, 401)
