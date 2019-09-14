from rest_framework import serializers
from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('__all__')


class WorkerModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = WorkerRole
        fields = ('__all__')
