from rest_framework import serializers
from .models import Author, Category, Book, Member, Record


# class AuthorSerilalizer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ('author_name',)
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('category_name',)


class BookSerializer(serializers.ModelSerializer):
    Author = serializers.CharField(source='author_name.author_name')
    Category = serializers.CharField(source='category_name.category_name')

    class Meta:
        model = Book
        fields = ('book_name', 'book_price', 'isbn_no', 'Author', 'Category')


# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member
#         fields = '__all__'
#
#
# class RecordSerializer(serializers.ModelSerializer):
#     Member = serializers.CharField(source='member_fname.member_fname')
#     Book = serializers.CharField(source='book_name.book_name')
#
#     class Meta:
#         model = Record
#         fields = '__all__'
