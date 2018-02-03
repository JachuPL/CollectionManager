from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'collections'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /collections/5/
    path('<int:collection_id>/', views.detail, name='detail'),
    path('<int:collection_id>/delete_collection/', views.delete_collection, name='delete_collection'),
    # ex: /collections/item/5
    path('create_collection/', views.create_collection, name='create_collection'),
    path('item/<int:value_id>/', views.item, name='item'),
]