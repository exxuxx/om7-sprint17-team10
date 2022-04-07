from unicodedata import name
from django import views
from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.authors, name='authors'),
    path('add', views.add_author, name='add_authors'),
    path('del', views.delete_authors, name='del_authors'),
    path('edit/<int:author_id>', views.edit_author, name="edit_author")
]
