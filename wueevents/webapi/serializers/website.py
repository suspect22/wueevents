from rest_framework import serializers

from webfrontent.models import Website


class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    """Displays Webiste Objects in Overview / List view"""

    class Meta:
        model = Website
        fields = ['id', 'url', 'title', 'enabled']
