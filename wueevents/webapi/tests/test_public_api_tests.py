from unittest import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class PublicApiTests(TestCase):
    """Holds all API Tests which will doesn't require authenticated Users"""

    API_ENDPOINT_WEBSITE = reverse("webapi:website-list")

    def setUp(self):
        self.unauthenticatedApiClient = APIClient()

    def test_unauthenticated_access_to_endpoint_website(self):
        """Tests if unauthenticated Access to the enpoint is possible"""
        response = self.unauthenticatedApiClient.get(self.API_ENDPOINT_WEBSITE)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
