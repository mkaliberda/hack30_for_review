from django.contrib import admin
from NaymikApi.apps.workers.models import WorkerRole, Education, Experience, WorkerSkill
# Register your models here.

admin.site.register(WorkerRole)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(WorkerSkill)