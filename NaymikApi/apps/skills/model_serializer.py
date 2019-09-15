from rest_framework import serializers
from NaymikApi.apps.skills.models import BaseSkill

class BaseSkillModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseSkill
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {
                'read_only': False, 
                'required': False
            },
            'name': {
                'read_only': False,
                'required': False
            }
        } #very important
