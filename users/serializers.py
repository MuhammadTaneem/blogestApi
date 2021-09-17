from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
