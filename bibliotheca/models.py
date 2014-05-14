from django.db import models
from django.db import models
import datetime
# Create your models here.

class Readers(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_blocked = models.BooleanField()

class Publishers(models.Model):
    name = models.CharField(max_length=255)

class Categories(models.Model):
    name = models.CharField(max_length=255)
    top_category_id = models.IntegerField()

class Books(models.Model):
    publisher_id = models.ForeignKey(Publishers)
    category_id = models.ForeignKey(Categories)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    published_date = models.DateTimeField('Data wydania')
    number_of_pages = models.IntegerField()
    description = models.TextField()

class Borrowings(models.Model):
    reader_id = models.ForeignKey(Readers)
    book_id = models.ForeignKey(Books)
    date_since = models.DateTimeField('Data wypożyczenia')
    date_to = models.DateTimeField('Data zwrotu')

class Authors(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Books_Authors(models.Model):
    author_id = models.ForeignKey(Authors)
    book_id = models.ForeignKey(Books)

class Books_Categories(models.Model):
    category_id = models.ForeignKey(Categories)
    boook_id = models.ForeignKey(Books)

class Warehouse(models.Model):
    book_id = models.ForeignKey(Books)
    books_quantity = models.IntegerField()
    books_available = models.IntegerField()
    books_reserved = models.IntegerField()

class News(models.Model):
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField('Data utworzenia')
    modification_date = models.DateTimeField('Data modyfikacji')
    text_body = models.TextField()

class Reservations(models.Model):
    reader_id = models.ForeignKey(Readers)
    book_id = models.ForeignKey(Books)
    reservation_date = models.DateTimeField('Data rezerwacji')

