from .models import Population, Category, Item
from rest_framework import serializers


class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Population
        fields = ('id', 'country', 'city', 'population')
        read_only_fields = ('id', 'country', 'city', 'population', )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'categories', 'value_int', 'value_float')
