from rest_framework import serializers
import os
from django.contrib.auth import authenticate
from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.workers.models import WorkerRole
from NaymikApi.apps.employers.models import EmployerRole

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'phone')

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username',
                  'password',
                  'is_worker',
                  'is_employer')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_worker': {'required': True},
            'is_employer': {'required': True}
            }

    def create(self, validated_data):
        user = CustomUser.objects.create(username=validated_data['username'],
                                         password=validated_data['password'],
                                         is_employer=validated_data['is_worker'],
                                         is_worker=validated_data['is_worker'])
        if user.is_employer:
            EmployerRole.objects.create(user=user)
        else:
            WorkerRole.objects.create(user=user)
        return user