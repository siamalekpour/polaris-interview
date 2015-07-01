from rest_framework.serializers import ModelSerializer
from trips.models import *


class ContinentSerializer(ModelSerializer):
    class Meta:
        model = Continent
        fields = ('id', 'name',)


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'continent',)


class TripTypeSerializer(ModelSerializer):
    class Meta:
        model = TripType
        fields = ('id', 'name',)


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id', 'name', 'type', 'country',)