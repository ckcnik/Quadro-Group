from django.conf.urls import include, url
from django.contrib import admin
from .views import set_session
from .api_views import PopulationList, CategoryViewSet, ItemViewSet, AuthView, LogoutView


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
    url(r'^api/stat/$', PopulationList.as_view(), name='population'),
    # категории
    url(r'^api/category/$', category_list, name='categories'),
    url(r'^api/category/(?P<pk>[0-9]+)/$', category_detail, name='category-detail'),
    # товары
    url(r'^api/item/$', item_list, name='items'),
    url(r'^api/item/(?P<pk>[0-9]+)/$', item_detail, name='item_detail'),
    # Аутентификация
    url(r'^set-session/$', set_session, name='set-session'),
    url(r'^api/login/$', AuthView.as_view(), name='login'),
    url(r'^api/logout/$', LogoutView.as_view(), name='logout'),
]
