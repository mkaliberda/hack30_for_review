from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.response import Response

from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience

from NaymikApi.apps.workers.model_serializer import WorkerModelSerializer

class WorkerRoleListView(generics.ListAPIView): # DetailView CreateView FormView
    # lookup_field = 'hash' # slug, id # url(r'?P<pk>\d+')
    queryset = WorkerRole.objects.all()
    serializer_class = WorkerModelSerializer

class WorkerRoleViewRetriveList(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet): # DetailView CreateView FormView
    # lookup_field = 'hash' # slug, id # url(r'?P<pk>\d+')
    serializer_class = WorkerModelSerializer
    lookup_field = 'worker_id'

    def get_queryset(self):
        return WorkerRole.objects.all()

    def get_object(self):
        return WorkerRole.objects.get(user__id=self.kwargs['user_id'])
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
        

