from django.urls import path, re_path, include
from NaymikApi.api.v1.workers.api import WorkerRoleViewRetriveList

urlpatterns = [
   re_path(r'^workers/', WorkerRoleViewRetriveList.as_view({'get': 'list'})),
   re_path(r'^worker/(?P<user_id>.+)/', WorkerRoleViewRetriveList.as_view(
      {'get': 'retrieve', 'patch':'update'}
   )),
]