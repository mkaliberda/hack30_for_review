from django.db import models

# Create your models here.

class BaseSkill(models.Model):
    name=models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'base_skill'
        verbose_name = 'base_skill'
        verbose_name_plural = 'base_skill'