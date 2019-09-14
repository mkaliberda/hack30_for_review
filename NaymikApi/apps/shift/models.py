from django.db import models

# Create your models here.

class WorkerSkill(models.Model):
    user=models.ForeignKey(to=CustomUser, related_name='base_skills_custom_user', on_delete=models.CASCADE, blank=False, null=False)
    base_skill = models.ForeignKey(to=BaseSkill, related_name='base_skills_base_skill', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'worker_skill'
        verbose_name = 'worker_skill'
        verbose_name_plural = 'worker_skill'