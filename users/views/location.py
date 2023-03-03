from rest_framework.viewsets import ModelViewSet

from users.models import Location
from users.serializers.location import LocationSerializer


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
