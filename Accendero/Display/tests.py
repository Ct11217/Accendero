import requests
import sqlite3
from django.test import TestCase
from Display.models import Item, ForecastEntry


class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(item="1001", item_desc="Test Item Description 1")
        Item.objects.create(item="1002", item_desc="Test Item Description 2")

    def test_item_setup(self):
        self.assertIsInstance(Item.objects.get(item="1001"), Item)
        self.assertIsInstance(Item.objects.get(item="1002"), Item)
        AssertionError("Error creating Item Class Objects")


class ForecastTestCase(TestCase):
    def setUp(self):
        Item.objects.create(item="10001", item_desc="Test Item Description 1")
        test_item1 = Item.objects.get(item="10001")
        for month in range(1, 13):
            ForecastEntry.objects.create(forecast_item=test_item1, month=month, quantity=500)

    def test_forecast_setup(self):
        forecast_entries = ForecastEntry.objects.filter(forecast_item=Item.objects.get(item="10001"))

        self.assertEqual(len(forecast_entries), 12)
        AssertionError("Error creating ForecastEntry Class Objects")

    def test_cascade_deletion(self):
        Item.delete(Item.objects.get(item="10001"))

        try:
            forecast_entries = ForecastEntry.objects.filter(forecast_item=Item.objects.get(item="10001"))
        except:
            forecast_entries = []

        self.assertEqual(len(forecast_entries), 0)
        AssertionError("Error in cascade deletion of ForecastEntry Class Objects")


class IntegrationApi(TestCase):
    def test_items_get(self):
        r = requests.get('http://localhost:8000/api/items/')
        self.assertEqual(r.status_code, 200)

    def test_forecast_get(self):
        r = requests.get('http://localhost:8000/api/forecasts/')
        self.assertEqual(r.status_code, 200)
