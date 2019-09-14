import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_worker = models.BooleanField(verbose_name='is_worker', default=False)
    is_employer = models.BooleanField(verbose_name='is_employer', default=False)
    phone = PhoneNumberField(default='', null=True, blank=True)

    class Meta:
        db_table = 'custom_user'
        verbose_name = 'custom_user'
        verbose_name_plural = 'custom_users'