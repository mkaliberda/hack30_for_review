from rest_framework import serializers
from rest_framework import serializers
from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.employers.models import EmployerRole
from NaymikApi.apps.skills.model_serializer import BaseSkillModelSerializer
from NaymikApi.apps.custom_users.model_serializer import UserModelSerializer


class EmployerModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = EmployerRole
        fields = ('user', 'company_name', 'company_address',
                  'company_logo', 'company_description')