from xml.etree.ElementInclude import include
from django import views
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'authentication'

router = routers.DefaultRouter()
router.register('', views.UserView)

router_book = routers.DefaultRouter()
router_book.register('', views.BookView)

router_order = routers.DefaultRouter()
router_order.register('', views.OrderView)

router_author = routers.DefaultRouter()
router_author.register('', views.AuthorView)

router_order_user = routers.DefaultRouter()
router_order_user.register('', views.OrderOfUserView)

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('add', views.add_user, name='add_user'),
    path('debtors', views.debtors, name='debtors'),
    path('del', views.delete_users, name='delete_users'),
    path('<int:id>', views.user_form, name='user_form'),
    path('api/v1/user/', include(router.urls)),
    path('api/v1/book/', include(router_book.urls)),
    path('api/v1/order/', include(router_order.urls)),
    path('api/v1/author/', include(router_author.urls)),
    path('api/v1/user/<int:user_id>/order/', include(router_order_user.urls))
]
