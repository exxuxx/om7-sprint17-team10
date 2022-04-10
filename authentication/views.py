from django.shortcuts import render
from rest_framework import generics, viewsets

from authentication.serializers import AuthorSerializer, OrderOfUserSerializer, OrderSerializer, UserSerializer
from book.serializers import BookSerializer
from order.models import *
from order.models import Order


class UserCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class BookCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class UserOrderCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        user_id = self.kwargs['user_id']
        user = CustomUser.objects.get(id=user_id)
        if user is not None:
            queryset = queryset.filter(user=user)
        else:
            queryset = []

        return queryset


class UserOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        user_id = self.kwargs['user_id']
        user = CustomUser.objects.get(id=user_id)
        if user is not None:
            queryset = queryset.filter(user=user)
        else:
            queryset = []

        return queryset


class OrderCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class AuthorCreateView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


def index(request):
    return render(request, 'pages/index.html')
