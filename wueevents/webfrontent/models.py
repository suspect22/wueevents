from django.db import models


# Create your models here.

class Website(models.Model):
    SCHEDULE_DAILY = 'D'
    SCHEDULE_HOURLY = 'H'
    SCHEDULE_WEEKLY = 'W'

    SCHEDULE_CHOICES = [
        (SCHEDULE_DAILY, 'Daily'),
        (SCHEDULE_HOURLY, 'Hourly'),
        (SCHEDULE_WEEKLY, "Weekly")
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

    def __str__(self):
        return "%s | %s | %s" % (self.title, self.schedule, self.enabled)