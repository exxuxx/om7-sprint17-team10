from django import views
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'book'

router = routers.DefaultRouter()
router.register('book', views.BookView)

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<int:book_id>', views.book_by_id, name="book_by_id"),
    path('create', views.create_library, name="create_library"),
    path('find', views.find_book, name="find_book"),
    path('api', include(router.urls))
]
