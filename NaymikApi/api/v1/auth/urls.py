from django.urls import path, re_path, include
from NaymikApi.api.v1.auth.api import LoginAPI, RegistrationAPI

urlpatterns = [
   re_path(r'^login/', LoginAPI.as_view()),
   re_path(r'^sign_up/', RegistrationAPI.as_view()),
]