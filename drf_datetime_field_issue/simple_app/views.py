from rest_framework import viewsets

from simple_app import models
from simple_app import serializers


class SimpleModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.SimpleModel.objects.all()
    serializer_class = serializers.SimpleModelSerializer


class MainModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = models.MainModel.objects.all()
    serializer_class = serializers.MainModelSerializer
