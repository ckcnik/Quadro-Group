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
