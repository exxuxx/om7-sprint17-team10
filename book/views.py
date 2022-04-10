from django.shortcuts import redirect, render
from . import models
from author import models as author_models
import csv
from django import forms
from random import randint
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from book import serializers

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookIdForm(forms.Form):
    book_id = forms.IntegerField()

class BookByAuthor(forms.Form):
    author_id = forms.IntegerField()

class SortBooks(forms.Form):
    sort_by = forms.ChoiceField(choices=[('1', "name(asc)"), ('2', "name(desc)"), ('3', "count")])

class FindBook(forms.Form):
    book_id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=20, required=False)
    author = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=50, required=False)

class UpdateBook(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=50, required=False)
    count = forms.IntegerField(required=False)

class AddBook(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    author = forms.CharField(max_length=20, required=True)
    description = forms.CharField(max_length=50, required=True)
    count = forms.IntegerField(required=True)



def all_books(request):
    all_books = models.Book.get_all()
    if request.method == "GET":
        all_books = models.Book.get_all()
        context = {
        "books": all_books,
        "form": BookIdForm(), 
        "form2": SortBooks(),
        "add_new_book": AddBook()
        }
        return render(request, "pages/all_books.html", context) 
    else:
        form = BookIdForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data["book_id"]
            return book_by_id(request, book_id)
        form2 = SortBooks(request.POST)
        if form2.is_valid():
            sort_method = form2.cleaned_data["sort_by"]
            if sort_method == '1':
                all_books = models.Book.objects.all().order_by("name")
            elif sort_method == '2':
                all_books = models.Book.objects.all().order_by("-name")
            else:
                all_books = models.Book.objects.all().order_by("count")
        form_add_book = AddBook(request.POST)
    
        if form_add_book.is_valid():
            name = form_add_book.cleaned_data["name"]
            author = form_add_book.cleaned_data["author"]
            description = form_add_book.cleaned_data["description"]
            count = form_add_book.cleaned_data["count"]
            created_author = author_models.Author.create(name = author, surname = author, patronymic = author)
            author_obj = author_models.Author.objects.get(name = author)
            book = models.Book.create(name = name, description = description, authors = [author_obj], count=count)
            all_books = models.Book.get_all()
        context = {
        "books": all_books,
        "form": BookIdForm(),
        "form2": SortBooks(),
        "add_new_book": AddBook() 
        }    
        return render(request, "pages/all_books.html", context)

def book_by_id(request, book_id):
    book = models.Book.get_by_id(book_id)
    if request.method == "GET":
        book = models.Book.get_by_id(book_id)
    else:
        form = UpdateBook(request.POST)
        if form.is_valid():
            update_name = form.cleaned_data["name"]
            update_description = form.cleaned_data["description"]
            update_count = form.cleaned_data["count"]
            book.update(name=update_name, description=update_description, count=update_count)
    return render(request, "pages/book.html", {
        "book": book,
        "form_update": UpdateBook()
    })
    
def find_book(request):
    context = { 
        "form3": FindBook(),
        "form_author_id": BookByAuthor(),
    }
    if request.method == "POST":        
        form = FindBook(request.POST)
        form_author_id = BookByAuthor(request.POST)

        if form.is_valid():
            book_id = form.cleaned_data["book_id"]
            name = form.cleaned_data["name"]
            author = form.cleaned_data["author"]
            description = form.cleaned_data["description"]
            context["show_author"] = False
            if book_id:
                return book_by_id(request, book_id)
            if name:
                book_name_search = models.Book.objects.filter(name__icontains = name)
                context["book_name_search"] = book_name_search
            if author:
                author_search = author_models.Author.objects.filter(name__icontains = author).first()
                book_author_search = author_search.books.all()
                context["book_author_search"] = book_author_search
            if description:
                description_search = models.Book.objects.filter(description__icontains = description)
                context["description_search"] = description_search
        
        if form_author_id.is_valid():
            author_id_data = form_author_id.cleaned_data["author_id"]
            author_by_id = author_models.Author.get_by_id(author_id_data)
            context["show_author"] = True
            if author_by_id == None:
                context["author_id_error"] = True
                context["author_by_id_error"] = author_id_data
            else:        
                context["author_by_id"] = author_by_id
                books_by_author = author_by_id.books.all()
                context["books_by_author"] = books_by_author    
        return render(request, "pages/find_book.html", context)    
    else:
        return render(request, "pages/find_book.html", context)



def create_library(request):
    with open("books.csv", newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            created_author = author_models.Author.create(name = row[2], surname = row[2], patronymic = row[2])
            author = author_models.Author.objects.get(name = row[2])
            book = models.Book.create(name = row[1], description = row[3], authors = [author], count=randint(1, 10))
    return redirect('book:all_books')

