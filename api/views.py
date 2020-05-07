import random

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TipSerializer

from .models import Tip

# API Views

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/tips/',
        'Get tip': '/get-tip/<str:id>/',
        'Random tip': '/random-tip/',
        'Create new tip': '/create-tip/',
        'Delete a tip': '/delete-tip/<str:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def tipList(request):

    tips = Tip.objects.all()
    serializer = TipSerializer(tips, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def randTip(request, ):

    limit = Tip.objects.all().count()
    n = random.randint(1, limit)

    tip = Tip.objects.get( id=n )
    serializer = TipSerializer(tip, many=False)

    return Response(serializer.data) 

@api_view(['GET'])
def getTip(request, pk):

    tip = Tip.objects.get( id=pk )
    serializer = TipSerializer(tip, many=False)

    return Response(serializer.data) 

@api_view(['POST'])
def createTip(request):

    serializer = TipSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 


@api_view(['GET', 'DELETE'])
def deleteTip(request, pk):

    tip = Tip.objects.get( id=pk )
    serializer = TipSerializer(tip, many=False)
    tip.delete()

    return Response(serializer.data)