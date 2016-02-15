from rest_framework import generics, viewsets, pagination
from .models import Population, Category, Item
from .serializers import PopulationSerializer, CategorySerializer, ItemSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class PopulationList(generics.ListAPIView):
    """
    API endpoint that represents a list of population cities.
    """
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of categories.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = StandardResultsSetPagination
