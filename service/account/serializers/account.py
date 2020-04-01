from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class AccountCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'email': {
                'required': True,
            },
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_password(self, password):
        validate_password(password)

        if self.instance is None:
            return password

        return make_password(password)


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )
