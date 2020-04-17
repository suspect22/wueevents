from django.test import TestCase
from webfrontent.models import Website, ScheduledElement, ElementMapping
from datetime import datetime, date
from django.db.utils import IntegrityError


class TestModels(TestCase):
    """Defines Tests which observes the models"""

    VALID_WEBSITE = {
        'title': 'Testwebsite',
        'url': 'https://ard.de',
        'schedule': Website.SCHEDULE_DAILY,
        'start_date': date.today(),
        'enabled': False
    }

    def create_sample_mapping(
            self,
            website,
            html_element="#StartDate > a",
            name=ElementMapping.STARTDATE
        ):
        output_element = ElementMapping.objects.create(
            website=website,
            html_element=html_element,
            name=name
        )
        return output_element

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
            website=website, scheduled_date=datetime.now())
        self.assertIn(website.title, str(scheduled_element_under_test))
        self.assertIn(
                      str(scheduled_element_under_test.scheduled_date),
                      str(scheduled_element_under_test)
                 )

    def test_calendar_mapping_string_representation(self):
        """Test that the string reprentation includes Website name and \
            Element Mapping"""
        website = Website.objects.create(**self.VALID_WEBSITE)
        calendar_mapping_under_test = ElementMapping.objects.create(
            website=website,
            html_element="#someRandomIdElement",
            name=ElementMapping.SUMMARY
        )

        self.assertIn(website.title, str(calendar_mapping_under_test))
        self.assertIn(ElementMapping.SUMMARY, str(calendar_mapping_under_test))

    def test_calendar_mapping_unique_constraint(self):
        """Test that a dulicate mapping for a Field does not exist"""
        website = Website.objects.create(**self.VALID_WEBSITE)
        ElementMapping.objects.create(
            website=website,
            html_element="#someRandomIdElement",
            name=ElementMapping.SUMMARY
        )

        with self.assertRaises(IntegrityError):
            ElementMapping.objects.create(
                website=website,
                html_element="#anotherRadomIdElement",
                name=ElementMapping.SUMMARY
            )

    def test_website_crawler_setup_is_valid(self):
        """
        Test that all required Mappings for a valid Website have
        to be available in is Mapping completed function
        """
        website = Website.objects.create(**self.VALID_WEBSITE)
        self.create_sample_mapping(website, name=ElementMapping.STARTDATE)
        self.create_sample_mapping(website, name=ElementMapping.ENDDATE)
        self.create_sample_mapping(website, name=ElementMapping.STARTTIME)
        self.assertTrue(website.isMappingComplete())

    def test_website_crawler_setup_is_invalid(self):
        """
        Test that isMapping complete does not return true if
        required Mappings are invalid
        """
        website = Website.objects.create(**self.VALID_WEBSITE)
        self.create_sample_mapping(website, name=ElementMapping.ENDDATE)
        self.create_sample_mapping(website, name=ElementMapping.STARTTIME)
        self.assertTrue(website.isMappingComplete())
