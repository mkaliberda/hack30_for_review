from rest_framework import serializers
from NaymikApi.apps.custom_users.models import CustomUser

class UserModelSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = CustomUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'phone',
                  'avatar')
