from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience

from NaymikApi.api.v1.workers.serializers import WorkerModelSerializer

class WorkerRoleListView(generics.ListAPIView): # DetailView CreateView FormView
    # lookup_field = 'hash' # slug, id # url(r'?P<pk>\d+')
    queryset = WorkerRole.objects.all()
    serializer_class = WorkerModelSerializer
