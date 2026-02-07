from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_facts(request):
    data = [
        {"id":1,"fact":"The sun is a star."},
        {"id":2,"fact":"Water boils at 100°C."},
        {"id":3,"fact":"Earth has one moon."}
    ]
    return Response(data)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Django Backend Running Successfully")
