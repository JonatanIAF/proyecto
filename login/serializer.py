#librerias de framwork
from rest_framework import routers, serializers, viewsets

#agregando modelos 
from login.models import Example2

class Example2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')