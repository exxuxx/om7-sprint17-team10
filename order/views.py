from django.shortcuts import redirect, render
from .models import *
from authentication.models import *
from book.models import *
import datetime
from django import forms
# Create your views here.

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {'user', 'book', 'end_at', 'plated_end_at'}
        lables = {
            'user': 'User',
            'book': 'Book',
            'end_at': 'End date',
            'plated_end_at': 'Plated End Date' 
        }

def orders_list(request,ord_by='created_at'):
    all_orders = Order.objects.all().order_by(ord_by)
    context = {
        'orders': all_orders
    }
    return render(request, 'pages/orders.html',context)


def add_order(request):
    random_user = CustomUser.objects.order_by('?')[0]
    random_book = Book.objects.order_by('?')[0]
    date = datetime.datetime.now() + datetime.timedelta(days=15)
    Order.create(random_user,random_book,date)
    return redirect('order:orders')


def add_neg_order(request):
    random_user = CustomUser.objects.order_by('?')[0]
    random_book = Book.objects.order_by('?')[0]
    date = datetime.datetime.now() + datetime.timedelta(days= -15)
    Order.create(random_user,random_book,date)
    return redirect('order:orders')


def orders_by_user_id(request,id):
    user = CustomUser.objects.get(id=id)
    orders = Order.objects.filter(user = id)
    context = {
        'orders':orders
    }
    return render(request,'pages/orders_by_user.html',context)

def del_order(request,id):
    Order.delete_by_id(id)
    return redirect('order:orders')

def un_ord(request):
    all_in = []
    all_out = []
    all_books = Book.objects.all()
    all_orders = Order.objects.all()
    for order in all_orders:
        all_in.append(order.book)
    for book in all_books:
        if book not in all_in:
            all_out.append(book)
    context={
        "books":all_out
    }
    return render(request,'pages/un_ordered_books.html',context)

def show_order(request, order_id=0):
    # form = OrderForm()
    # order = Order.get_by_id(order_id)
    # context = {
    #     "order": order,
    #     "form": form
    # }
    # return render(request, "pages/order_form.html", context)

    if request.method == "GET":
        if order_id == 0:
            form = OrderForm()
        else: 
            order = Order.get_by_id(order_id)
            form = OrderForm(instance=order)
        return render(request, "pages/order_form.html", context = {
            "form": form,
            "id": id
        })
    else:
        if order_id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.get_by_id(order_id)
            form = OrderForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
    return redirect('order:orders')
    
