from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=100,help_text='Enter the author name')

    def __str__(self):
        return self.author_name

class Category(models.Model):
    category_name = models.CharField(max_length=100,help_text='Enter the books category')

    def __str__(self):
        return self.category_name

class Book(models.Model):
    book_name = models.CharField(max_length=100,help_text='Enter the name of the book')
    book_price = models.IntegerField(help_text='Enter the price of the book')
    isbn_no = models.IntegerField()
    author_name = models.ForeignKey(Author,on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

class Member(models.Model):
    member_fname = models.CharField(max_length=100,help_text='Enter the first name')
    member_lname = models.CharField(max_length=100,help_text='Enter the last name')
    member_phoneno = models.IntegerField(help_text='Enter the phone number')
    member_email = models.EmailField(help_text='Enter the valid email')

    def __str__(self):
        return self.member_fname

class Record(models.Model):
    member_fname = models.ForeignKey(Member,on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.member_fname)

