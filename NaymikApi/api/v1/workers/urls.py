from django.urls import path, re_path, include
from NaymikApi.api.v1.workers.api import WorkerRoleListView

urlpatterns = [
   re_path(r'^', WorkerRoleListView.as_view()),
]