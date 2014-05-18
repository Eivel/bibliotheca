from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Readers(models.Model):
    user = models.OneToOneField(User)
    address_street = models.CharField(max_length=255)
    address_strno = models.IntegerField()
    address_aptno = models.IntegerField(null=True, blank=True)
    address_postcode = models.CharField(max_length=7)
    address_city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    is_blocked = models.BooleanField(default=False)

class Publishers(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=255)
    top_category_id = models.IntegerField(null=True, blank=True)
    is_main_category = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    publisher_id = models.ForeignKey(Publishers)
    category_id = models.ForeignKey(Categories)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    published_date = models.DateTimeField('Data wydania')
    number_of_pages = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Borrowings(models.Model):
    reader_id = models.ForeignKey(Readers)
    book_id = models.ForeignKey(Books)
    date_since = models.DateTimeField('Data wypożyczenia')
    date_to = models.DateTimeField('Data zwrotu')

class Authors(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' ' + self.last_name

class Books_Authors(models.Model):
    author_id = models.ForeignKey(Authors)
    book_id = models.ForeignKey(Books)

    def __str__(self):
        return self.author_id.name + ' ' + self.author_id.last_name + ' - ' + self.book_id.title

class Warehouse(models.Model):
    book_id = models.ForeignKey(Books)
    books_quantity = models.IntegerField()
    books_available = models.IntegerField()
    books_reserved = models.IntegerField()

class News(models.Model):
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField('Data utworzenia')
    modification_date = models.DateTimeField('Data modyfikacji', null=True, blank=True)
    text_body = models.TextField()

class Reservations(models.Model):
    reader_id = models.ForeignKey(Readers)
    book_id = models.ForeignKey(Books)
    reservation_date = models.DateTimeField('Data rezerwacji')
