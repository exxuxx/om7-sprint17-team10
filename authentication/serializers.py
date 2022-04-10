from attr import field
from rest_framework import serializers
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from author.models import Author

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'authors', 'count')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'patronymic')

class OrderOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at')
