from django.contrib import admin
from store.models import Population


class PopulationAdmin(admin.ModelAdmin):
    """
    Модель Population
    """
    list_display = ('country', 'city', 'population')
admin.site.register(Population, PopulationAdmin)
