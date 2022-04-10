from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now

from authentication.models import CustomUser
from book.models import Book
from order.models import Order
from .models import *
import string
import random
from .forms import *
# Create your views here.


def authors(request):
    authors_list = Author.objects.all()
    context = {
        'authors': authors_list
    }
    return render(request, "pages/authors.html", context)


def add_author(request):
    letters = string.ascii_lowercase
    for_author = []
    for i in range(3):
        word = ''.join(random.choice(letters)for i in range(4, 10))
        for_author.append(word)
    Author.create(
        name=for_author[0], surname=for_author[1], patronymic=for_author[2])
    # if request.method == "POST":
    #     form = AddAuthor(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("all_books")
    # else:
    #     form = AddAuthor()
#    return render(request, 'pages/add_author.html')
    return redirect('authors:authors')


def delete_authors(request):
    all_authors = Author.objects.all()
    all_authors.delete()
    return redirect('authors:authors')


def edit_author(request, author_id):
    if request.method == "GET":
        if id == 0:
            form = EditAuthor()
        else:
            author = Author.get_by_id(author_id)
            form = EditAuthor(instance=author)
        return render(request, "pages/edit_author.html", context={"form": form, "id": author_id})
    else:
        author = Author.get_by_id(author_id)
        form = EditAuthor(request.POST, instance=author)
    if form.is_valid():
        form.save()
    return redirect("authors:authors")


def fill(self):
    Order.objects.all().delete()
    Author.objects.all().delete()
    Book.objects.all().delete()
    CustomUser.objects.all().delete()

    user = CustomUser(id=111, email='email@mail.com', password='1234', first_name='fname',
                           middle_name='mname',
                           last_name='lname')
    user.save()
    user_free = CustomUser(id=222, email='2email@mail.com', password='1234', first_name='2fname',
                                middle_name='2mname',
                                last_name='2lname')
    user_free.save()

    author1 = Author(id=101, name="author1", surname="s1", patronymic="p1")
    author1.save()

    author2 = Author(id=102, name="author2", surname="s2", patronymic="p2")
    author2.save()

    book1 = Book(id=101, name="book1", description="description1", count=1)
    book1.save()
    book1.authors.add(author1)
    book1.save()

    book2 = Book(id=102, name="book2", description="description2", count=15)
    book2.save()
    book2.authors.add(author2)
    book2.save()

    book3 = Book(id=103, name="book3", description="description3")
    book3.save()
    book3.authors.add(author1)
    book3.authors.add(author2)
    book3.save()

    order1 = Order(id=101, user=user, book=book1, end_at="2021-01-01 10:30:20", plated_end_at='2021-01-02 10:30:20')
    order1.save()
    order2 = Order(id=102, user=user, book=book2, plated_end_at=now())
    order2.save()
    order3 = Order(id=103, user=user, book=book3, end_at=now(), plated_end_at=now())
    order3.save()

    return HttpResponse('Done')
