from django import views
from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('add', views.add_user, name='add_user'),
    path('debtors', views.debtors, name='debtors'),
    path('del', views.delete_users, name='delete_users'),
    path('<int:id>', views.user_form, name='user_form')
]