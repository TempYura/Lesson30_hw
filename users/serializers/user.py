from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer, SlugRelatedField, ManyRelatedField

from users.models.location import Location
from users.models.user import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class UserListSerializer(ModelSerializer):
    total_ads = IntegerField()

    class Meta:
        model = User
        fields = ['id', 'username', 'total_ads']


class UserDetailSerializer(ModelSerializer):
    locations = SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = User
        exclude = ["password"]
