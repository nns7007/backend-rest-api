from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from api_project import serializers
from api_project import models
from api_project import permissions

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello msg"""

        a_viewset = [
            'uses actions-list,create,retrive,update,partial_update',
            'maps to urls using routers automatically',
            'provide more funt. with less code',
        ]

        return Response({'message': 'Hello!','a_viewset': a_viewset})

    def create(self,request):
        """create hello msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle to get obj by its ID"""
        return Response({'http_method': 'GET'})

    def update(self,request,pk=None):
        """Handle the update to object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self,request,pk=None):
        """Handle to update obj partially"""
        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):
        """Handle to remove an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating & updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """create user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
