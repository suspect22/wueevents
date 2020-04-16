from django.contrib import admin

# Register your models here.
from webfrontent.models import Website, ScheduledElement
from webfrontent.models import ElementMapping

admin.site.register(Website)
admin.site.register(ScheduledElement)
admin.site.register(ElementMapping)
