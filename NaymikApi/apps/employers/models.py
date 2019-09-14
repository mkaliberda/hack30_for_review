from django.db import models
from NaymikApi.apps.custom_users.models import CustomUser

# Create your models here.


class EmployerRole(models.Model):
    user = models.ForeignKey(to=CustomUser,
                             related_name='employer_role_custom_user',
                             on_delete=models.CASCADE, blank=False, null=False)

    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='companies/logos', default='')
    company_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        db_table = 'employer_role'
        verbose_name = 'employer_role'
        verbose_name_plural = 'employer_roles'

