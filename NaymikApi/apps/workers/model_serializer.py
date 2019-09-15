from rest_framework import serializers
from NaymikApi.apps.custom_users.model_serializer import UserModelSerializer
from NaymikApi.apps.skills.model_serializer import BaseSkillModelSerializer
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience
from NaymikApi.apps.skills.models import BaseSkill


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
                  'educations_worker_role',
                  'experiences_worker_role',
                  'base_skills_worker_role')

    @property
    def data(self):
        db_data = super().data
        return {
            'first_name': db_data['user']['first_name'],
            'last_name': db_data['user']['last_name'],
            'photo': db_data['user']['avatar'],
            'phone_number': db_data['user']['phone'],
            'education': db_data['educations_worker_role'],
            'experience': db_data['experiences_worker_role'],
            'roles': db_data['base_skills_worker_role'],
        }

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        education_data = validated_data.pop('education', {})
        experience_data = validated_data.pop('experience', {})
        base_skills_worker_role = validated_data.pop('base_skills_worker_role', {})

        for key, value in user_data.items():
            setattr(instance.user, key, value)

        for key, value in education_data.items():
            setattr(instance.education, key, value)

        for key, value in experience_data.items():
            setattr(instance.experience, key, value)

        all_roles = instance.base_skills_worker_role_set.all()
        all_roles_mapping_id_name = {role['name']:role['id'] for role in all_roles}

        for key, value in all_roles_mapping_id_name:
            if key not in base_skills_worker_role:
                WorkerRole.objects.filter(id=value).delete()

        for key in base_skills_worker_role:
            if key not in all_roles_mapping_id_name:
                WorkerRole.objects.create(user=instance, name=key)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.user.save()
        instance.save()
        return instance
