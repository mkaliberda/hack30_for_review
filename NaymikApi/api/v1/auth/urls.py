from django.urls import path, re_path, include
from NaymikApi.api.v1.auth.api import LoginAPI

urlpatterns = [
   re_path(r'^login/', LoginAPI.as_view()),
]