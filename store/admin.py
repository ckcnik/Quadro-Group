from django.contrib import admin
from store.models import Population, Category, Item


class PopulationAdmin(admin.ModelAdmin):
    """
    Модель Population
    """
    list_display = ('country', 'city', 'population')
admin.site.register(Population, PopulationAdmin)


class CategoryAdmin(admin.ModelAdmin):
    """
    Модель категорий
    """
    list_display = ('name', 'description')
admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    """
    Модель товаров (Item)
    """
    list_display = ('name', 'value_int', 'value_float')
admin.site.register(Item, ItemAdmin)
