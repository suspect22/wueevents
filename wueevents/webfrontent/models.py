from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now

class Website(models.Model):
    """Model to create Websites which will be crawled"""
    SCHEDULE_DAILY = 'D'
    SCHEDULE_HOURLY = 'H'
    SCHEDULE_WEEKLY = 'W'

    SCHEDULE_CHOICES = [
        (SCHEDULE_DAILY, _('Daily')),
        (SCHEDULE_HOURLY, _('Hourly')),
        (SCHEDULE_WEEKLY, _("Weekly"))
    ]

    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    enabled = models.BooleanField(default=True)
    schedule = models.CharField(
        max_length=1, choices=SCHEDULE_CHOICES, default=SCHEDULE_WEEKLY
    )
    start_date = models.DateField()
    latitude = models.CharField(max_length=20, default="49.000", blank=True)
    longitude = models.CharField(max_length=20, default="9.000", blank=True)
    street = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    location = models.CharField(max_length=200, null=True)

    def __str__(self):
        """ String Representation which will be used in List views """
        return "%s | %s | %s" % (self.title, self.schedule, self.enabled)

    def create_instant_run(self):
        """ """


class WebsiteElementMapping(models.Model):
    """Model to create Element Mappings between Calendar and Crawler"""

    class Meta:
        unique_together = (("name","website"))

    # Enum like field for Mapping Ical Calendar Elements to displayed values
    SUMMARY = 'summary'
    STARTDATE = 'dtstart'
    ENDDATE = 'dtend'
    STARTTIME = 'tstart'
    ENDTIME = 'tend'
    LINK = 'link'
    DETAILS = 'details'

    # Elements Display Mapping
    ELEMENT_CHOICES = {
        (SUMMARY, _("Summary")),
        (STARTDATE, _("Start Date")),
        (ENDDATE, _("End Date")),
        (STARTTIME, _("Start Time")),
        (ENDTIME, _("End Time")),
        (LINK, _("Source Link")),
        (DETAILS, _("Details"))
    }

    website = models.ForeignKey(
        Website,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=20,
        choices=ELEMENT_CHOICES,
        default=SUMMARY,
    )
    html_element = models.CharField(max_length=50)
    # start_time = None
    # end_time=None
    # summary=None
    # organizer=None
    # title=None
    # external_link=None
    # longitude=None
    # latitute=None

    def __str__(self):
        return f'%s | %s' % (getattr(self.website, "title"), self.name)


class CrawlerQueueElement(models.Model):
    """Scheduled Crawl object which displays crawl Schedules"""
    website = models.ForeignKey(
        Website,
        on_delete=models.CASCADE
    )
    logs = models.TextField(
        default="Run has not been started"
        )
    last_run = models.DateTimeField(blank=True, null=True)
    next_run = models.DateTimeField()

    def __str__(self):
        """String representation used in List views """
        return "%s | %s" % (getattr(self.website, 'title'),
                            str(self.next_run))


class CrawlerRun(models.Model):
    """Element which persists the runs of the crawler into the database"""
    exit_code = models.IntegerField(default=-1)
    execution_time = models.DateTimeField()
    schedule_element = models.ForeignKey(
        CrawlerQueueElement,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        """ String Representation used in List views """
        pass
