from django.db import models
from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.skills.models import BaseSkill

# Create your models here.


class Shift(models.Model):
    user = models.ForeignKey(to=CustomUser, related_name='shift_custom_user', on_delete=models.SET_NULL, blank=False, null=True)
    employer = models.ForeignKey(to=CustomUser, related_name='shift_employer', on_delete=models.SET_NULL, blank=False, null=True)
    uniform = models.ImageField()
    workers_number = models.IntegerField()
    salary = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'shift'
        verbose_name = 'shift'
        verbose_name_plural = 'shift'


class Schedule(models.Model):
    shift = models.ForeignKey(to=Shift, related_name='schedule_shift', on_delete=models.CASCADE, blank=False, null=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)


class ShiftSkill(models.Model):
    shift_role = models.ForeignKey(to=Shift,
                                   related_name='base_skills_shift_role',
                                   on_delete=models.CASCADE,
                                   blank=False, null=False)
    base_skill = models.ForeignKey(to=BaseSkill,
                                   related_name='shift_skills_base_skill',
                                   on_delete=models.CASCADE,
                                   blank=False, null=False)

    def __str__(self):
        return f'worker_role: {self.shift_role}, skill: {self.base_skill}'

    class Meta:
        db_table = 'shift_skill'
        verbose_name = 'shift_skill'
        verbose_name_plural = 'shift_skill'
