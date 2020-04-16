from rest_framework import serializers

from webfrontent.models import ScheduledElement


class ScheduledElementSerializer(serializers.HyperlinkedModelSerializer):
    """Displays Webiste Objects in Overview / List view"""

    class Meta:
        model = ScheduledElement
        fields = ['id', 'scheduled_date', 'website']
