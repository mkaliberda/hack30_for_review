from rest_framework import serializers
from rest_framework import serializers
from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.employers.models import EmployerRole
from NaymikApi.apps.skills.model_serializer import BaseSkillModelSerializer
from NaymikApi.apps.custom_users.model_serializer import UserModelSerializer


class EmployerModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    id = serializers.UUIDField(source='user.id', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    phone = serializers.CharField(source='user.phone', read_only=True)
    avatar = serializers.CharField(source='user.avatar', read_only=True)

    class Meta:
        model = EmployerRole
        fields = ('user', 'company_name', 'company_address',
                  'company_logo', 'company_description') + UserModelSerializer.Meta.fields

    @property
    def data(self):
        db_data = super().data
        return {
            'first_name': db_data['user']['first_name'],
            'last_name': db_data['user']['last_name'],
            'phone_number': db_data['user']['phone'],
            'company_name': db_data['company_name'],
            'company_address': db_data['company_address'],
            'company_description': db_data['company_description'],
        }

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})

        for key, value in user_data.items():
            setattr(instance.user, key, value)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.user.save()
        instance.save()
        return instance