from django.contrib.auth.models import User, Group
from rest_framework import serializers

from webfrontent.models import Website


class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'url', 'title', 'enabled']
