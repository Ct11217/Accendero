from django.middleware import csrf
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ItemSerializer, ForecastEntrySerializer
from .models import Item, ForecastEntry


def index(request):
    return HttpResponse("Hello django!")


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ForecastView(viewsets.ModelViewSet):
    serializer_class = ForecastEntrySerializer
    queryset = ForecastEntry.objects.all()
