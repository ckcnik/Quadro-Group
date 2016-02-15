from django.conf.urls import include, url
from django.contrib import admin
from .views import PopulationList, CategoryViewSet, ItemViewSet


category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

item_list = ItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
item_detail = ItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^app/api/stat/$', PopulationList.as_view(), name='population'),
    # категории
    url(r'^app/api/category/$', category_list, name='categories'),
    url(r'^app/api/category/(?P<pk>[0-9]+)/$', category_detail, name='category-detail'),
    # товары
    url(r'^app/api/item/$', item_list, name='items'),
    url(r'^app/api/item/(?P<pk>[0-9]+)/$', item_detail, name='item_detail'),
]
