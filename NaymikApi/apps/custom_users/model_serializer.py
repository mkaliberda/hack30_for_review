from rest_framework import serializers
from NaymikApi.apps.custom_users.models import CustomUser

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'is_worker', 'is_employer', 'phone', 'avatar')
