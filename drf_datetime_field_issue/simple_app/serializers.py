from rest_framework import serializers

from simple_app import models


class MainModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MainModel


class SimpleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SimpleModel
