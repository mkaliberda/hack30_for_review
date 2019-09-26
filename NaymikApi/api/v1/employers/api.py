from rest_framework import viewsets, permissions, generics, mixins, status

from NaymikApi.apps.employers.models import EmployerRole

from NaymikApi.apps.employers.model_serializer import EmployerModelSerializer
from rest_framework.response import Response


class EmployerRoleViewRetriveList(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet): # DetailView CreateView FormView
    # lookup_field = 'hash' # slug, id # url(r'?P<pk>\d+')
    serializer_class = EmployerModelSerializer
    lookup_field = 'employer_id'

    def get_queryset(self):
        return EmployerRole.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = EmployerModelSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        serializer = EmployerModelSerializer(self.get_object())
        return Response(serializer.data)

    def get_object(self):
        return EmployerRole.objects.get(user__id=self.kwargs['user_id'])

    def update(self, request, *args, **kwargs):
        user_data = request.data
        user_to_update = self.get_object()
        # Here is that serialize, validate, save pattern we talked about
        # before.

        serializer_data = {
            'user': {
                'first_name': user_data.get('first_name'),
                'last_name': user_data.get('last_name'),
                'phone': user_data.get('')
            },
            'company_name': user_data.get('company_name'),
            'company_address': user_data.get('company_address'),
            'company_description': user_data.get('company_description'),
        }

        #pass request.user here
        serializer = self.serializer_class(
            user_to_update, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


