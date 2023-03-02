from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models.selection import Selection
from users.models.user import User


class SelectionSerializer(ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(queryset=User.objects.all(), slug_field="username", required=False)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = "__all__"
