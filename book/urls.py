from django import views
from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<int:book_id>', views.book_by_id, name="book_by_id"),
    path('create', views.create_library, name="create_library"),
    path('find', views.find_book, name="find_book")
]
