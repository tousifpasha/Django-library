from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    Author=serializers.CharField(source='author_name')
    Category=serializers.CharField(source='category_name')

    class Meta:
        model = Book
        fields = ('pk','book_name','book_price','isbn_no','Author','Category')


class BookCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('book_name','book_price','isbn_no','author_name','category_name')

class BookDestroySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('book_name','book_price','isbn_no','author_name','category_name')
        
class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('book_name','book_price','isbn_no','author_name','category_name')