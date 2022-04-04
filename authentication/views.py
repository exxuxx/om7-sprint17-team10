from django.shortcuts import redirect, render
from .models import *
from order.models import *
import string
import random

def users(request):
    context = {
        'users' : CustomUser.objects.all()
    }
    return render(request,'pages/users.html',context)


def index(request):
    return render(request,'pages/index.html')

def add_user(request):
    letters = string.ascii_lowercase
    for_user = []
    for i in range(4):
        word = ''.join(random.choice(letters)for i in range(4,10))
        for_user.append(word)
    emails = []
    for i in range(1):
        my_email = ''.join(random.choice(letters) for i in range(5,10))+'@gmail.com'
        emails.append(my_email)
        new_user = CustomUser.create(first_name=for_user[0],middle_name=for_user[1],last_name=for_user[2],password=for_user[3],email=emails[i])
    return redirect('authentication:users')


def debtors(request):
    res = []
    all_orders = Order.objects.all()
    for order in all_orders:
        if order.created_at >= order.plated_end_at:
            res.append(order.user)
    context = {
        'users' : res
    }
    return render(request,'pages/debtor_users.html',context)


def delete_users(request):
    for_delete = CustomUser.objects.all()
    for_delete.delete()
    return redirect('authentication:users')