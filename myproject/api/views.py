from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import Itemserializers


@api_view(['GET'])
def getData(request):
    Items = Item.objects.all()
    serializer = Itemserializers(Items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = Itemserializers(data=request.data)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)