from django.db import models
from django.utils.translation import gettext as _


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
    latitude = models.CharField(max_length=20, null=True)
    longitude = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    location = models.CharField(max_length=200, null=True)

    def isMappingComplete(self):
        raise NotImplementedError

    def __str__(self):
        return "%s | %s | %s" % (self.title, self.schedule, self.enabled)


class ElementMapping(models.Model):

    class Meta:
        unique_together = (("name", "website"))

    """Model to create Element Mappings between Calendar and Crawler"""
    ALLEVENTS='allEvents'
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

    def __str__(self):
        return f'%s | %s' % (getattr(self.website, "title"), self.name)


class ScheduledElement(models.Model):
    """Scheduled Crawl object which displays crawl Schedules"""
    website = models.ForeignKey(
        Website,
        on_delete=models.CASCADE
    )
    scheduled_date = models.DateTimeField()

    def __str__(self):
        return "%s | %s" % (getattr(self.website, 'title'),
                            str(self.scheduled_date))

