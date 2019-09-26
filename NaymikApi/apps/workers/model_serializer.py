from rest_framework import serializers
from NaymikApi.apps.custom_users.model_serializer import UserModelSerializer
from NaymikApi.apps.skills.model_serializer import BaseSkillModelSerializer
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience
from NaymikApi.apps.skills.models import BaseSkill

class WorkerSkillModelSerializer(serializers.ModelSerializer):
    role = BaseSkillModelSerializer(source='base_skill')

    class Meta:
        model = WorkerSkill
        fields = ('id', 'role')
        extra_kwargs = {
            'id': {
                'read_only': True,
                'required': False
            },
            'role': {
                'read_only': True,
                'required': False
            }
        } #very important

    @property
    def data(self):
        db_data = super().data
        return {
            'skill': db_data['base_skill']['name'],
            'id': db_data['base_skill']['id'],
        }


class EducationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'name', 'start_date', 'end_date', 'is_present', 'faculty')
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
            },
            'faculty': {
                'read_only': False,
                'required': False
            }
        } #very important


class ExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'name', 'start_date', 'end_date', 'is_present', 'position')
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
            },
            'position': {
                'read_only': False,
                'required': False
            }
        }

import json

class WorkerListSerializer(serializers.ListSerializer):

    @property
    def data(self):
        return [{
            'first_name': db_data['user']['first_name'],
            'last_name': db_data['user']['last_name'],
            'photo': db_data['user']['avatar'],
            'phone_number': db_data['user']['phone'],
            'education': db_data['educations_worker_role'],
            'experience': db_data['experiences_worker_role'],
            'skills_roles': db_data['skills_roles'],
        } for db_data in super().data]

class WorkerModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    educations_worker_role = EducationModelSerializer(many=True)
    experiences_worker_role = ExperienceModelSerializer(many=True)
    skills_roles = BaseSkillModelSerializer(many=True)
    # base_skills_worker_role = WorkerSkillModelSerializer(many=True)

    class Meta:
        model = WorkerRole
        fields = ('user',
                  'city',
                  'rate',
                  'skills_roles',
                  'educations_worker_role',
                  'experiences_worker_role')
        list_serializer_class = WorkerListSerializer

    @property
    def data(self):
        db_data = super().data
        return {
            'city': db_data['city'],
            'rate': db_data['rate'],
            'first_name': db_data['user']['first_name'],
            'last_name': db_data['user']['last_name'],
            'photo': db_data['user']['avatar'],
            'phone_number': db_data['user']['phone'],
            'education': db_data['educations_worker_role'],
            'experience': db_data['experiences_worker_role'],
            'skills_roles': db_data['skills_roles'],
        }

    def validate_skills_roles(self, roles):
        print('roles', roles)
        return roles

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        education_data = validated_data.pop('educations_worker_role', {})
        experience_data = validated_data.pop('experiences_worker_role', {})
        roles_data = validated_data.pop('skills_roles', {})

        for key, value in user_data.items():
            setattr(instance.user, key, value)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.user.save()
        instance.save()
        education_before = Education.objects.filter(worker_role=instance)
        for item in education_before:
            item.delete()

        for item in education_data:
            Education.objects.create(worker_role=instance,
                                     name=item.get('name', ''),
                                     start_date=item.get('start_date', None),
                                     end_date=item.get('end_date', None),
                                     is_present=item.get('is_present', False),
                                     faculty=item.get('faculty', ''))
        experience_before = Experience.objects.filter(worker_role=instance)

        for item in experience_before:
            item.delete()

        for item in experience_data:
            Experience.objects.create(worker_role=instance,
                                      name=item.get('name', ''),
                                      start_date=item.get('start_date', None),
                                      end_date=item.get('end_date', None),
                                      is_present=item.get('is_present', False),
                                      position=item.get('position', ''))

        instance.skills_roles.clear()
        for item in roles_data:
            try:
                skill = BaseSkill.objects.get(id=item['id'])
            except Exception as e:
                pass
            else:
                instance.skills_roles.add(skill)
        #TODO DROP AND CREATE experience_data

       #TODO set roles

        return instance
