from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest-fr/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^app/', include('app.urls')),
]
