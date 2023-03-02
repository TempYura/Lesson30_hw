from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer, SlugRelatedField, ManyRelatedField

from users.models.location import Location
from users.models.user import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserCreateSerializer(ModelSerializer):
    locations = SlugRelatedField(required=False, slug_field='name', many=True, queryset=Location.objects.all())

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        password = validated_data.pop("password")
        new_user = User.objects.create(**validated_data)
        new_user.set_password(password)
        new_user.save()

        for loc in self._location:
            location, _ = Location.objects.get_or_create(name=loc)
            new_user.locations.add(location)
        return new_user

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
