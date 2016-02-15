from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Population(models.Model):
    """
    Таблица численности населения по городам и странам
    """
    country = models.CharField(max_length=100, verbose_name=_(u'Country'))
    city = models.CharField(max_length=100, verbose_name=_(u'City'))
    population = models.IntegerField(verbose_name=_(u'Population'))

    def __str__(self):
        return self.country


@python_2_unicode_compatible
class Category(models.Model):
    """
    Таблица категорий
    """
    name = models.CharField(max_length=100, verbose_name=_(u'Name'))
    description = models.TextField(blank=True, verbose_name=_(u'Description'))

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Item(models.Model):
    """
    Таблица товаров
    """
    name = models.CharField(max_length=100, verbose_name=_(u'Name'))
    categories = models.ManyToManyField(Category)
    value_int = models.PositiveIntegerField(verbose_name=_(u'Number'))
    value_float = models.FloatField(verbose_name=_(u'Cost'))

    def __str__(self):
        return self.name
