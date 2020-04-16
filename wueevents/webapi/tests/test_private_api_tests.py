from unittest import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model


class PrivateApiTests(TestCase):
    """Holds all API Tests which will doesn't require authenticated Users"""

    API_ENDPOINT_WEBSITE = reverse("webapi:website-list")
    API_ENDPOINT_SCHEDULEDELEMENT = reverse("webapi:scheduledelement-list")

    def setUp(self):
        self.apiClient = APIClient()
        self.authenticatedUser = get_user_model().objects.create_user(
            username="testuser",
            email="testemail@bla.com",
            password="TestPassword123"
        )
        self.apiClient.force_authenticate(self.authenticatedUser)

    def test_create_website(self):
        pass

    def test_create_website_with_invalid_values(self):
        pass

    def test_create_scheduled_element(self):
        pass

    def test_create_scheduled_element_with_invalid_values(self):
        pass

    def tearDown(self):
        self.authenticatedUser.delete()
