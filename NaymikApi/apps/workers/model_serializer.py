from rest_framework import serializers
from NaymikApi.apps.custom_users.model_serializer import UserModelSerializer
from NaymikApi.apps.skills.model_serializer import BaseSkillModelSerializer
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience



class WorkerSkillModelSerializer(serializers.ModelSerializer):
    base_skill = BaseSkillModelSerializer()

    class Meta:
        model = WorkerSkill
        fields = ('id', 'base_skill')
        extra_kwargs = {
            'id': {
                'read_only': True, 
                'required': False
            },
            'base_skill': {
                'read_only': False, 
                'required': False
            }
        } #very important


class EducationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'name', 'start_date', 'end_date', 'is_present')
        extra_kwargs = {
            'id': {
                'read_only': True, 
                'required': False
            },
            'name': {
                'read_only': False, 
                'required': False
            },
            'start_date': {
                'read_only': False, 
                'required': False
            },
            'end_date': {
                'read_only': False, 
                'required': False
            },
            'is_present': {
                'read_only': False, 
                'required': False
            }
        } #very important

class ExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'name', 'start_date', 'end_date', 'is_present')
        extra_kwargs = {
            'id': {
                'read_only': True, 
                'required': False
            },
            'start_date': {
                'read_only': False, 
                'required': False
            },
            'end_date': {
                'read_only': False,
                'required': False
            },
            'is_present': {
                'read_only': False,
                'required': False
            }
        }

class WorkerModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    education = EducationModelSerializer(many=True, source='education_worker_role')
    experiences_worker_role = ExperienceModelSerializer(many=True)
    base_skills_worker_role = WorkerSkillModelSerializer(many=True)
    education = serializers.CharField(source='educations_worker_role')

    class Meta:
        model = WorkerRole
        fields = ('user',
                   'city',
                   'rate',
                   'education',
                   'experiences_worker_role',
                   'base_skills_worker_role')

        extra_kwargs = {
            'id': {
                'read_only': True, 
                'required': False
            },
            'city': {
                'read_only': False, 
                'required': False
            },
            'rate': {
                'read_only': False, 
                'required': False
            },
            'educations_worker_role': {
                'read_only': False, 
                'required': False
            },
            'experiences_worker_role': {
                'read_only': False, 
                'required': False
            },
            'base_skills_worker_role': {
                'read_only': False, 
                'required': False
            },
        }

    def update(self, instance, validated_data):
        # Update the  instance
        print(instance)
        instance.save()
        return instance