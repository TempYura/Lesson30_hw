from rest_framework.serializers import ModelSerializer

from users.models.location import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
