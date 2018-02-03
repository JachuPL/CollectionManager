from django.urls import path
from . import views

app_name = 'collections'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /collections/5/
    path('<int:collection_id>/', views.detail, name='detail'),
    # ex: /collections/item/5
    path('item/<int:value_id>/', views.item, name='item'),
    # ex: /register/
    path('register/', views.register, name='register'),
    # ex: /login/
    path('login/', views.login_user, name='login'),
    # ex: /logout/
    path('logout/', views.logout_user, name='logout'),

]