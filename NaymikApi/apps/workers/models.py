from django.db import models
from NaymikApi.apps.skills.models import BaseSkill
from NaymikApi.apps.custom_users.models import CustomUser
# Create your models here.

class WorkerRole(models.Model):
    user=models.ForeignKey(to=CustomUser,
                           related_name='worker_role_custom_user',
                           on_delete=models.CASCADE,
                           blank=False, null=False)
    city=models.CharField(max_length=100, blank=True, null=True)
    rate=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        db_table = 'worker_role'
        verbose_name = 'worker_role'
        verbose_name_plural = 'worker_role'

class Education(models.Model):
    worker_role=models.ForeignKey(to=WorkerRole,
                                  related_name='educations_worker_role',
                                  on_delete=models.CASCADE,
                                  blank=False, null=False)
    name=models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'custom_user_education'
        verbose_name = 'custom_user_education'
        verbose_name_plural = 'custom_user_education'


class Experience(models.Model):
    worker_role=models.ForeignKey(to=WorkerRole,
                                  related_name='experiences_worker_role',
                                  on_delete=models.CASCADE,
                                  blank=False, null=False)
    name=models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'custom_user_experience'
        verbose_name = 'custom_user_experience'
        verbose_name_plural = 'custom_user_experience'
    

class WorkerSkill(models.Model):
    worker_role=models.ForeignKey(to=WorkerRole,
                                  related_name='base_skills_worker_role',
                                  on_delete=models.CASCADE,
                                  blank=False, null=False)
    base_skill = models.ForeignKey(to=BaseSkill,
                                   related_name='base_skills_base_skill',
                                   on_delete=models.CASCADE,
                                   blank=False, null=False)

    def __str__(self):
        return f'worker_role: {self.worker_role}, skill: {self.base_skill}'

    class Meta:
        db_table = 'worker_skill'
        verbose_name = 'worker_skill'
        verbose_name_plural = 'worker_skill'
