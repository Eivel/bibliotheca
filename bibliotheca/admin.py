from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from bibliotheca.models import *
import datetime
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'creation_date', 'modification_date', 'text_body']
    search_fields = ['title', 'text_body']

class BooksAdmin(admin.ModelAdmin):
    search_fields = ['title', 'original_title', 'ISBN', 'publisher__name', 'authors__last_name']
    fields = ['title', 'original_title', 'publisher', 'category', 'authors', 'ISBN', 'published_date', 'number_of_pages', 'description']
    list_display = ['title', 'category', 'publisher', 'authors_all', 'ISBN']

    def authors_all(self, instance):
        return ",".join(a.last_name + " " + a.name for a in instance.authors.all())
    authors_all.short_description = 'Autorzy'


class PublishersAdmin(admin.ModelAdmin):
    fields = ['name']

class AuthorsAdmin(admin.ModelAdmin):
    fields = ['name', 'last_name']
    search_fields = ['name', 'last_name']

class CategoriesAdmin(admin.ModelAdmin):
    fields = ['name', 'top_category']
    search_fields = ['name']

class ReservationsAdmin(admin.ModelAdmin):
    fields = ['reader', 'book', 'reservation_date']
    search_fields = ['reader__user__first_name', 'reader__user__last_name']
    actions = ['borrow', 'delete']
    def delete_reservations(self, request, queryset):
        for q in queryset:
            warehouse = Warehouse.objects.get(book=q.book.book_id)
            warehouse.books_reserved -= 1
            warehouse.books_available += 1
            warehouse.save()
        queryset.delete()
        self.message_user(request, "Zaznaczone rezerwacje zostały usunięte, a stan książek uaktualniony")
    def borrow(self, request, queryset):
        for q in queryset:
            borrowing = Borrowings()
            borrowing.reader = q.reader
            borrowing.book = q.book
            borrowing.date_since = datetime.datetime.now()
            duration = datetime.timedelta(days = 90)
            borrowing.date_to = borrowing.date_since + duration
            borrowing.save()
        rows_updated = len(queryset)
        queryset.delete()
        if rows_updated == 1:
            message_bit = "1 książka została"
            self.message_user(request, "%s wypożyczona." % message_bit)
        else:
            message_bit = "%s książek zostało" % rows_updated
            self.message_user(request, "%s wypożyczonych." % message_bit)
    borrow.short_description = "Wypożycz zaznaczone książki"
    delete_reservations.short_destription = "Usuń zaznaczone rezerwacje"

class BorrowingsAdmin(admin.ModelAdmin):
    fields = ['reader', 'book', 'date_since', 'date_to']
    search_fields = ['reader__user__first_name', 'reader__user__last_name']
    actions = ['borrow', 'delete']
    def delete_borrowings(self, request, queryset):
        for q in queryset:
            warehouse = Warehouse.objects.get(book=q.book.book_id)
            warehouse.books_reserved -= 1
            warehouse.books_available += 1
            warehouse.save()
        queryset.delete()
        self.message_user(request, "Zaznaczone wypożyczenia zostały usunięte, a stan książek uaktualniony")
    delete_borrowings.short_destription = "Usuń zaznaczone wypożyczenia"

class WarehouseAdmin(admin.ModelAdmin):
    fields = ['book', 'books_quantity', 'books_available', 'books_reserved']

class ReadersInline(admin.StackedInline):
    model = Readers

class UserAdmin(OriginalUserAdmin):
    inlines = [ReadersInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'address', 'is_blocked',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_blocked', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Groups'), {'fields': ('groups',)}),
    )

    def address(self, instance):
        reader = Readers.objects.get(user=instance)

        address = "ul. " + reader.address_street + " " + str(reader.address_strno)

        if reader.address_aptno:
            address += "/" + str(reader.address_aptno)

        address += ", " + reader.address_postcode + " " + reader.address_city

        return address
    address.short_description = 'Adres pocztowy'

    def is_blocked(self, instance):
        reader = Readers.objects.get(user=instance)

        return reader.is_blocked
    is_blocked.short_description = 'Czy zablokowany?'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(News, NewsAdmin)
admin.site.register(Books,BooksAdmin)
admin.site.register(Publishers,PublishersAdmin)
admin.site.register(Authors,AuthorsAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Reservations,ReservationsAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Borrowings, BorrowingsAdmin)