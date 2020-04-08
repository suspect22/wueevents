from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from webapi.serializers import WebsiteSerializer
from webfrontent.models import Website


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Website.objects.all().order_by('id')
    serializer_class = WebsiteSerializer
    permission_classes = [permissions.IsAuthenticated]
