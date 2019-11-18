from django.contrib import admin

# Register your models here.
from libraryapp.models import Book, Author, Category, Member, Record

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_price', 'isbn_no', 'author_name', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('book_name',)
    ordering_by = ('book_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Member)
admin.site.register(Record)