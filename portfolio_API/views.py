from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def allAPIView(request):
    api_urls = {
        'Projects API' : '/projects/',
        'Skills API': '/skills/',
        'Contacts API': '/contact/',
    }
    return Response(api_urls)
