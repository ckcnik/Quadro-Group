from django.conf.urls import include, url
from django.contrib import admin
from .views import PopulationList


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^app/api/stat/$', PopulationList.as_view(), name='population'),
]
