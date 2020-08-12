from django.conf.urls import url
from basic_app import views

app_name='basic_apps'

urlpatterns=[
    url(r'^relative/$',views.relative_fun,name='relative'),
    url(r'^other/$',views.other_fun,name='other_vy'),
]
