from django.urls import path
from . import views

app_name = 'collections'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /collections/5/
    path('<int:collection_id>/', views.detail, name='detail'),
    path('<int:collection_id>/delete_collection/', views.delete_collection, name='delete_collection'),
    path('<int:collection_id>/edit_collection/', views.edit_collection, name='edit_collection'),
    path('<int:collection_id>/create_item/', views.create_item, name='create_item'),
    # ex: /collections/item/5
    path('create_collection/', views.create_collection, name='create_collection'),
    path('item/<int:value_id>/', views.item, name='item'),
    # ex: /register/
    path('register/', views.register, name='register'),
    # ex: /login/
    path('login/', views.login_user, name='login'),
    # ex: /logout/
    path('logout/', views.logout_user, name='logout'),
    path('item/<int:value_id>/delete_item/', views.delete_item, name='delete_item'),
    path('item/<int:value_id>/edit_item/', views.edit_item, name='edit_item'),
]