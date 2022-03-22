from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api_project import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializers_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return features of APIview in list format"""
        an_apiview = [
            'HTTP methods -get,post,patch,put,delete',
            'similar to django traditional view',
            'give control over you on application logic',
            'manually mapped to url',
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})

    def post(self,request):
        """create hello msg with our name"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Update the object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """partially update the object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
