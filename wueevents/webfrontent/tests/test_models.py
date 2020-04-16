from unittest import TestCase
from webfrontent.models import Website, WebsiteElementMapping
from webfrontent.models import CrawlerQueueElement, CrawlerRun
from django.utils.timezone import now
from django.db.utils import IntegrityError


class TestModels(TestCase):
    """Defines Tests which observes the models"""

    VALID_WEBSITE = {
        'title': 'Testwebsite',
        'url': 'https://ard.de',
        'schedule': Website.SCHEDULE_DAILY,
        'start_date': now(),
        'enabled': False
    }

    def test_website_string_representation(self):
        """Test that the string representation includes specific values"""
        website_under_test = Website.objects.create(**self.VALID_WEBSITE)
        stringRepresentation = str(website_under_test)

        self.assertIn(self.VALID_WEBSITE['title'], stringRepresentation)

    def test_crawler_queue_elements_string_representation(self):
        """Test that the string representation includes Website name and \
            Scheduled Date"""
        website = Website.objects.create(**self.VALID_WEBSITE)
        crawler_element_under_test = CrawlerQueueElement.objects.create(
            website=website,next_run=now())
        self.assertIn(website.title, str(crawler_element_under_test))
        self.assertIn(
                      str(crawler_element_under_test.next_run),
                      str(crawler_element_under_test)
                 )

    def test_website_calendar_mapping_string_representation(self):
        """Test that the string reprentation includes Website name and \
            Element Mapping"""
        website = Website.objects.create(**self.VALID_WEBSITE)
        calendar_mapping_under_test = WebsiteElementMapping.objects.create(
            website=website,
            html_element="#someRandomIdElement",
            name=WebsiteElementMapping.SUMMARY
        )

        self.assertIn(website.title, str(calendar_mapping_under_test))
        self.assertIn(WebsiteElementMapping.SUMMARY, str(calendar_mapping_under_test))

    def test_wesite_calendar_mapping_exists_only_one_time(self):
        """Test that a dulicate mapping for a Field does not exist"""
        website = Website.objects.create(**self.VALID_WEBSITE)
        WebsiteElementMapping.objects.create(
            website=website,
            html_element="#someRandomIdElement",
            name=WebsiteElementMapping.SUMMARY
        )

        with self.assertRaises(IntegrityError):
            WebsiteElementMapping.objects.create(
                website=website,
                html_element="#anotherRadomIdElement",
                name=WebsiteElementMapping.SUMMARY
            )

    def test_crawler_run_string_representation(self):
        """ 
        Test that the scheduled run Representation includes the 
        execution time and the website name
        """
        website = Website.objects.create(**self.VALID_WEBSITE)
        WebsiteElementMapping.objects.create(
            website=website,
            html_element="#someRandomElement"
        )