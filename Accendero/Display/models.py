from django.db import models


class Item(models.Model):
    item = models.BigIntegerField(primary_key=True)
    item_desc = models.CharField(max_length=500)

    def __int__(self):
        self.item


class ForecastEntry(models.Model):
    forecast_item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Month(models.IntegerChoices):
        January = 1,
        February = 2,
        March = 3,
        April = 4,
        May = 5,
        June = 6,
        July = 7,
        August = 8,
        September = 9,
        October = 10,
        November = 11,
        December = 12

    month = models.IntegerField(choices=Month.choices)
    quantity = models.BigIntegerField()
    date_modified = models.DateField(auto_now_add=True)

    def __int__(self):
        return self.forecast_item

    class Meta:
        unique_together = (("forecast_item", "month"),)




