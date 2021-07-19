from django.contrib.auth import get_user_model

from django.conf import settings
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user_model = get_user_model()
        instance = user_model.objects.create(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance
