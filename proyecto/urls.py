from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view),
    re_path(r'^',include(router.urls)),
    re_path(r'^api/v1/',include('login.urls')),
    re_path(r'^api/v1/',include('Profile.urls')),

]