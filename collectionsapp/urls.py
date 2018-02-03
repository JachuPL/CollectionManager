from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'collections'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /collections/5/
    path('<int:collection_id>/', views.detail, name='detail'),
    # ex: /collections/item/5
    path('item/<int:value_id>/', views.item, name='item'),

]