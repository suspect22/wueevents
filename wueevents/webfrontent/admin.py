from django.contrib import admin

# Register your models here.
from webfrontent.models import Website, WebsiteElementMapping
from webfrontent.models import CrawlerQueueElement, CrawlerRun

admin.site.register(Website)
admin.site.register(WebsiteElementMapping)
admin.site.register(CrawlerQueueElement)
admin.site.register(CrawlerRun)
