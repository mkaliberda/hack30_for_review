from rest_framework import serializers
from NaymikApi.apps.custom_users.models import CustomUser


class UserModelSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
        model = CustomUser
        fields = (
                  'first_name',
                  'last_name',
                  'phone',
                  'avatar')

    def update(self, instance, validated_data):
        instance.save()

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance