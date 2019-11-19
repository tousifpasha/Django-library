from django.contrib import admin

# Register your models here.
from libraryapp.models import Book, Author, Category, Member, Record
from django import forms

class AuthorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        author = self.cleaned_data.get('author_name')
        if len(author) < 4:
            raise forms.ValidationError('Please enter a valid name,name cannot be less than 4 characters', code = 'invalid')

        return self.cleaned.data
    def save(self, commit=True):
        return super(AuthorAdminForm, self).save(commit=commit)

class MemberAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        phoneno = self.cleaned_data.get('member_phoneno')
        if len(str(phoneno)) != 10:
            raise forms.ValidationError('Please enter a valid phone number', code='invalid')

        return self.cleaned.data

    def save(self, commit=True):
        return super(MemberAdminForm, self).save(commit=commit)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_price', 'isbn_no', 'author_name', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('book_name',)
    ordering = ('book_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('author_name',)
    ordering = ('author_name',)
    form = AuthorAdminForm

class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Record)