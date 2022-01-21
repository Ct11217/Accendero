from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item', 'item_desc')


#class ForecastEntry(serializers.ModelSerializer):
 #   class Meta:
  #      model = ForecastEntry
   #     fields = {'forecast_item', 'month', 'quantity', 'date_modified'}


