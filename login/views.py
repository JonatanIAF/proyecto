from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

#clase de lunes 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#importar modelo lunes 
from login.models import Example2
from login.serializer import Example2Serializers
  

#clase de lunes 
class ExampleList2(APIView):
    #metodo GET para solicitar info
    def get(self, request, format = None):
        print("metodo get filter")
        queryset = Example2.objects.filter(delete = False)
        #many = True  si aplica si retorno multiple objetos 
        serializer = Example2Serializers(queryset,many = True)
        return Response(serializer.data)


    def post(self, request, format):
        serializer = Example2Serializers(data = request.data)
        if serializer .is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)



# create your views here

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustonAuthToken(ObtainAuthToken):

    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data,
                                            context = {
                                                    'request': request,
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })