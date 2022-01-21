from django.contrib import admin

from .models import Item, ForecastEntry


class ForecastEntryInLine(admin.StackedInline):
    model = ForecastEntry
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["item", "item_desc"]})
    ]
    inlines = [ForecastEntryInLine]


admin.site.register(Item, ItemAdmin)
