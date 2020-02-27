#librerias Framework
from rest_framework import routers, serializers, viewsets

#agregando modelos

from Profile.models import ProfileP
from Profile.models import CiudadM
from Profile.models import GeneroM
from Profile.models import OcupacionM
from Profile.models import EstadoM
from Profile.models import Estado_civilM


class ExamplePSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileP
        fields = ('__all__')

class CiudadS(serializers.ModelSerializer):
    class Meta:
        model = CiudadM
        fields = ('__all__')

class GeneroS(serializers.ModelSerializer):
    class Meta:
        model = GeneroM
        fields = ('__all__')

class OcupacionS(serializers.ModelSerializer):
    class Meta:
        model = OcupacionM
        fields = ('__all__')

class EstadoS(serializers.ModelSerializer):
    class Meta:
        model = EstadoM
        fields = ('__all__')

class Estado_civilS(serializers.ModelSerializer):
    class Meta:
        model = Estado_civilM
        fields = ('__all__')