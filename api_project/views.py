from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self,request,format=None):
        """Return features of APIview in list format"""
        an_apiview = [
            'HTTP methods -get,post,patch,put,delete',
            'similar to django traditional view',
            'give control over you on application logic',
            'manually mapped to url',
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})
