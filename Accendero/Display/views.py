from django.middleware import csrf
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item


def index(request):
    return HttpResponse("Hello django!")

class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()