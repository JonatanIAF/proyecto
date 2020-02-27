from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

# from rest_framework import routers, serilizers, viewsets
from login.views import CustonAuthToken
from login.views import ExampleList2


urlpatterns = [
    re_path(r'login/$', CustonAuthToken.as_view()),
    #lunes 
    re_path(r'example_Lista2/$', ExampleList2.as_view()),
]