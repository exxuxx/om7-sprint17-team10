from django.urls import path
from . import views

from .views import UserCreateView, UserDetailView, BookCreateView, BookDetailView, AuthorDetailView, AuthorCreateView, \
    OrderDetailView, OrderCreateView, UserOrderCreateView, UserOrderDetailView
from django.urls import path

from . import views
from .views import UserCreateView, UserDetailView, BookCreateView, BookDetailView, AuthorDetailView, AuthorCreateView, \
    OrderDetailView, OrderCreateView, UserOrderCreateView, UserOrderDetailView

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),

    path('api/v1/user/<int:user_id>/order/', UserOrderCreateView.as_view()),
    path('api/v1/user/<int:user_id>/order/<int:pk>', UserOrderDetailView.as_view()),

    path('api/v1/user/', UserCreateView.as_view()),
    path('api/v1/user/<int:pk>', UserDetailView.as_view()),

    path('api/v1/book/', BookCreateView.as_view()),
    path('api/v1/book/<int:pk>', BookDetailView.as_view()),

    path('api/v1/order/', OrderCreateView.as_view()),
    path('api/v1/order/<int:pk>', OrderDetailView.as_view()),

    path('api/v1/author/', AuthorCreateView.as_view()),
    path('api/v1/author/<int:pk>', AuthorDetailView.as_view()),

]
