from django.contrib import admin

# Register your models here.
from webfrontent.models import Website, ScheduledElement

admin.site.register(Website)
admin.site.register(ScheduledElement)