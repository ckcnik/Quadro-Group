from rest_framework import generics
from .models import Population
from .serializers import PopulationSerializer


class PopulationList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of population cities.
    """
    model = Population
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer
