from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^auth/', include('NaymikApi.api.v1.auth.urls')),
    re_path(r'^', include('NaymikApi.api.v1.workers.urls')),
    re_path(r'^', include('NaymikApi.api.v1.employers.urls')),
]