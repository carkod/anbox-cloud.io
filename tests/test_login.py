from vcr_unittest import VCRTestCase, VCRMixin
import vcr
from webapp.app import ANBOXCLOUD_API_BASE
import requests
from webapp import app
import unittest


class TestLogin(VCRMixin, VCRTestCase):

    def setUp(self):
        """
        Set up Flask app for testing
        """
        app.testing = True
        self.client = app.test_client()

    @vcr.use_cassette()
    def test_login(self):

        response = requests.get(f"{ANBOXCLOUD_API_BASE}/1.0/token", params={"provider": "usso"})
        # Test that we have a cassete
        self.assertEqual(len(self.cassette), 1)
        # Rest of tests
        self.assertEqual(self.cassette)
