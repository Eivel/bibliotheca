from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import pdb
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

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Publishers(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=255)
    top_category = models.ForeignKey('self', null=True, blank=True)
    #is_main_category = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Categories.objects.filter(top_category=self):
            r.append(c.get_all_children())
        return r

class Authors(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' ' + self.last_name

class Books(models.Model):
    publisher = models.ForeignKey(Publishers)
    category = models.ForeignKey(Categories)
    authors = models.ManyToManyField(Authors)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    published_date = models.IntegerField('Rok wydania')
    number_of_pages = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Borrowings(models.Model):
    reader = models.ForeignKey(Readers)
    book = models.ForeignKey(Books)
    date_since = models.DateTimeField('Data wypożyczenia')
    date_to = models.DateTimeField('Data zwrotu')


class Warehouse(models.Model):
    book = models.ForeignKey(Books)
    books_quantity = models.IntegerField()
    books_available = models.IntegerField()
    books_reserved = models.IntegerField()

    def __str__(self):
        return self.book.title

class News(models.Model):
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField('Data utworzenia')
    modification_date = models.DateTimeField('Data modyfikacji', null=True, blank=True)
    text_body = models.TextField()

    def __str__(self):
        return self.title

class Reservations(models.Model):
    reader = models.ForeignKey(Readers)
    book = models.ForeignKey(Books)
    reservation_date = models.DateTimeField('Data rezerwacji')

    def __str__(self):
        return self.reader.user.first_name + ' ' + self.reader.user.last_name + ' : ' + self.book.title

