from .models import User
from rest_framework import serializers


class UserSerialiser(serializers.ModelSerialiser):
    class Meta:
        model = User
        exclude = ("password",)


class UserCreateSerialiser(serializers.ModelSerialiser):
    class Meta:
        models = User
        fileds = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "bio",
            "image",
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
