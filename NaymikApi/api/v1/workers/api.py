from rest_framework import viewsets, permissions, generics, mixins, status
from rest_framework.response import Response

from NaymikApi.apps.custom_users.models import CustomUser
from NaymikApi.apps.workers.models import WorkerRole, WorkerSkill, Education, Experience

from NaymikApi.apps.workers.model_serializer import WorkerModelSerializer

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

    def retrieve(self, request, *args, **kwargs):
        serializer = WorkerModelSerializer(self.get_object())
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user_data = request.data
        user_to_update = self.get_object()
        # Here is that serialize, validate, save pattern we talked about
        # before.

        serializer_data = {
            'user': {
                'first_name': user_data.get('first_name'),
                'last_name': user_data.get('last_name'),
                'phone': user_data.get('phone_number'),
                'avatar': user_data.get('photo'),
            },
            'educations_worker_role': user_data.get('education'),
            'experiences_worker_role': user_data.get('experience'),
            'base_skills_worker_role': user_data.get('company_description'),
        }

        #pass request.user here
        serializer = self.serializer_class(
            user_to_update, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

