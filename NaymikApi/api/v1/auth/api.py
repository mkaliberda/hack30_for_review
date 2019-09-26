from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import LoginUserSerializer, UserSerializer, CreateUserSerializer
from NaymikApi.apps.custom_users.model_serializer import UserModelSerializer

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        AuthToken.objects.create(user)
        return Response({
            "user": UserModelSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[-1]
        })

class RegistrationAPI(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def get_queryset(self):
        return

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserModelSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[-1]
        })
