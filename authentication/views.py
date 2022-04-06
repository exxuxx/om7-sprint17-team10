from django.shortcuts import redirect, render
from .models import *
from order.models import *
import string
import random
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = {'first_name', 'last_name', 'middle_name', 'email'}
        lables = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'middle_name': 'Middle Name',
            'email': 'email' 
        }

def user_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else: 
            user = CustomUser.get_by_id(id)
            form = UserForm(instance=user)
        return render(request, "pages/user_form.html", context = {
            "form": form,
            "id": id
        })
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.get_by_id(id)
            form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
    return redirect('authentication:users')


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