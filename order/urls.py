from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('', views.orders_list, name='orders'),
    path('sort-<str:ord_by>', views.orders_list, name='sorted_order'),
    path('<int:id>', views.orders_by_user_id, name='orders_by_user_id'),
    path('add', views.add_order, name='add_order'),
    path('add_neg', views.add_neg_order, name='add_neg_order'),
    path('un_ord', views.un_ord, name='un_ordered'),
    path('del-<int:id>', views.del_order, name='del_order'),
    path('change/<int:order_id>', views.show_order, name='show_order')
]
