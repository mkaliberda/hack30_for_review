from rest_framework import serializers
from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.skills.model_serializer import BaseSkillModelSerializer
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience



class WorkerSkillModelSerializer(serializers.ModelSerializer):
    base_skill = BaseSkillModelSerializer()

    class Meta:
        model = WorkerSkill
        fields = ('id', 'base_skill')


class EducationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('name', 'start_date', 'end_date', 'is_present')

class ExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('name', 'start_date', 'end_date', 'is_present')

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'is_worker', 'is_employer', 'phone', 'avatar')

class WorkerModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    educations_worker_role = EducationModelSerializer(many=True)
    experiences_worker_role = ExperienceModelSerializer(many=True)
    base_skills_worker_role = WorkerSkillModelSerializer(many=True)

    class Meta:
        model = WorkerRole
        fields = ('user',
                   'city',
                   'rate',
                   'educations_worker_role',
                   'experiences_worker_role',
                   'base_skills_worker_role')