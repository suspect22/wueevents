from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from webapi.serializers.website import WebsiteSerializer
from webapi.serializers.scheduledelement import ScheduledElementSerializer
from webfrontent.models import Website, ScheduledElement


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Website.objects.all().order_by('id')
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.IsAuthenticated]


class ScheduledElementViewSet(viewsets.ModelViewSet):
     """
     API endpoint that allow Users to edit Elements
     """
     queryset = ScheduledElement.objects.all().order_by('-schedule_date')
     serializer_class = ScheduledElementSerializer
     permission_classes = [permissions.IsAuthenticated]
