from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import pdb
# Create your models here.

class Readers(models.Model):
    class Meta:
        verbose_name = 'Czytelnik'
        verbose_name_plural = 'Czytelnicy'

    user = models.OneToOneField(User)
    address_street = models.CharField('Ulica', max_length=255)
    address_strno = models.IntegerField('Nr domu')
    address_aptno = models.IntegerField('Nr mieszkania', null=True, blank=True)
    address_postcode = models.CharField('Kod pocztowy', max_length=7)
    address_city = models.CharField('Miejscowość', max_length=255)
    phone_number = models.CharField('Nr telefonu', max_length=12)
    is_blocked = models.BooleanField('Zablokowany', default=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Publishers(models.Model):
    class Meta:
        verbose_name = 'Wydawca'
        verbose_name_plural = 'Wydawcy'

    name = models.CharField(max_length=255,verbose_name='Nazwa wydawnictwa')

    def __str__(self):
        return self.name

class Categories(models.Model):
    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    name = models.CharField(max_length=255,verbose_name='Nazwa kategorii')
    top_category = models.ForeignKey('self', null=True, blank=True,verbose_name='Kategoria nadrzędna')
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
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'

    name = models.CharField(max_length=255,verbose_name='Imię autora')
    last_name = models.CharField(max_length=255,verbose_name='Nazwisko autora')

    def __str__(self):
        return self.name + ' ' + self.last_name

class Books(models.Model):
    class Meta:
        verbose_name = 'Książka'
        verbose_name_plural = 'Książki'

    publisher = models.ForeignKey(Publishers,verbose_name='Wydawca')
    category = models.ForeignKey(Categories,verbose_name='Kategoria')
    authors = models.ManyToManyField(Authors,verbose_name='Autorzy')
    title = models.CharField(max_length=255,verbose_name='Tytuł')
    original_title = models.CharField(max_length=255,verbose_name='Tytuł oryginalny',null=True, blank=True)
    ISBN = models.CharField(max_length=255)
    published_date = models.IntegerField('Rok wydania')
    number_of_pages = models.IntegerField('Liczba stron', null=True, blank=True)
    description = models.TextField('Opis', null=True, blank=True)
    cover = models.ImageField('Okładka', upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title

class Borrowings(models.Model):
    class Meta:
        verbose_name = 'Wypożyczenie'
        verbose_name_plural = 'Wypożyczenia'

    reader = models.ForeignKey(Readers)
    book = models.ForeignKey(Books)
    date_since = models.DateTimeField('Data wypożyczenia')
    date_to = models.DateTimeField('Data zwrotu')

    def __str__(self):
        return self.reader.user.first_name + ' ' + self.reader.user.last_name + ' : ' + self.book.title

class Warehouse(models.Model):
    class Meta:
        verbose_name = 'Magazyn'
        verbose_name_plural = 'Magazyny'

    book = models.ForeignKey(Books)
    books_quantity = models.IntegerField()
    books_available = models.IntegerField()
    books_reserved = models.IntegerField()

    def __str__(self):
        return self.book.title

class News(models.Model):
    class Meta:
        verbose_name = 'Wiadomość'
        verbose_name_plural = 'Wiadomości'

    title = models.CharField(max_length=255,verbose_name='Tytuł wiadomości')
    creation_date = models.DateTimeField('Data utworzenia')
    modification_date = models.DateTimeField('Data modyfikacji', null=True, blank=True)
    text_body = models.TextField(verbose_name='Treść wiadomości')

    def __str__(self):
        return self.title

class Reservations(models.Model):
    class Meta:
        verbose_name = 'Rezerwacja'
        verbose_name_plural = 'Rezerwacje'

    reader = models.ForeignKey(Readers)
    book = models.ForeignKey(Books)
    reservation_date = models.DateTimeField('Data rezerwacji')

    def __str__(self):
        return self.reader.user.first_name + ' ' + self.reader.user.last_name + ' : ' + self.book.title

class MailRemainder(models.Model):
    borrowing = models.ForeignKey(Borrowings)
    sent_mails = models.IntegerField()