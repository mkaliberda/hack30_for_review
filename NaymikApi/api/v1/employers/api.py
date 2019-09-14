from rest_framework import viewsets, permissions, generics, mixins

from NaymikApi.apps.employers.models import EmployerRole

from NaymikApi.apps.employers.model_serializer import EmployerModelSerializer


class EmployerRoleViewRetriveList(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet): # DetailView CreateView FormView
    # lookup_field = 'hash' # slug, id # url(r'?P<pk>\d+')
    serializer_class = EmployerModelSerializer
    lookup_field = 'employer_id'

    def get_queryset(self):
        return EmployerRole.objects.all()

    def get_object(self):
        return EmployerRole.objects.get(user__id=self.kwargs['user_id'])

