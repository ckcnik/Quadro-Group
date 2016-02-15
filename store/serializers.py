from .models import Population
from rest_framework import serializers


class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Population
        fields = ('id', 'country', 'city', 'population')
        read_only_fields = ('id', 'country', 'city', 'population', )
