from rest_framework import serializers
from .models import Item, ForecastEntry


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item', 'item_desc')


class ForecastEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForecastEntry
        fields = ('forecast_item', 'month', 'quantity', 'date_modified')


