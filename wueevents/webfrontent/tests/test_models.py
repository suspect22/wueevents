from unittest import TestCase
from webfrontent.models import Website, ScheduledElement
from django.db import models
from datetime import datetime,date


class TestModels(TestCase):
    """Defines Tests which observes the models"""

    VALID_WEBSITE = {
        'title': 'Testwebsite',
        'url': 'https://ard.de',
        'schedule': Website.SCHEDULE_DAILY,
        'start_date': date.today(),
        'enabled': False
    }

    def test_website_string_representation(self):
        """Test that the string representation includes specific values"""
        website_under_test = Website.objects.create(**self.VALID_WEBSITE)
        stringRepresentation = str(website_under_test)

        self.assertIn(self.VALID_WEBSITE['title'], stringRepresentation)

    def test_scheduled_elements_string_representation(self):
        """Test that the string representation includes Website name and \
            Scheduled Date"""
        website = Website.objects.create(**self.VALID_WEBSITE)
        scheduled_element_under_test = ScheduledElement.objects.create(
            website=website,
            scheduled_date=datetime.now()
        )
        self.assertIn(website.title, str(scheduled_element_under_test))
        self.assertIn(
                      str(scheduled_element_under_test.scheduled_date),
                      str(scheduled_element_under_test)
                 )