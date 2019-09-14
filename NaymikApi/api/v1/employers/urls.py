from django.urls import path, re_path, include
from NaymikApi.api.v1.employers.api import EmployerRoleViewRetriveList

urlpatterns = [
   re_path(r'^employers/', EmployerRoleViewRetriveList.as_view({'get': 'list'})),
   re_path(r'^employer/(?P<user_id>.+)/', EmployerRoleViewRetriveList.as_view({'get': 'retrieve', 'patch': 'update'})),
]