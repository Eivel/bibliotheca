from django.contrib import admin
from bibliotheca.models import *
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'creation_date', 'modification_date', 'text_body']

class BooksAdmin(admin.ModelAdmin):
    fields = ['publisher', 'category', 'authors', 'title', 'original_title', 'ISBN', 'published_date', 'number_of_pages', 'description']

class PublishersAdmin(admin.ModelAdmin):
    fields = ['name']

class AuthorsAdmin(admin.ModelAdmin):
    fields = ['name', 'last_name']

class CategoriesAdmin(admin.ModelAdmin):
    fields = ['name', 'top_category']


admin.site.register(News, NewsAdmin)
admin.site.register(Books,BooksAdmin)
admin.site.register(Publishers,PublishersAdmin)
admin.site.register(Authors,AuthorsAdmin)
admin.site.register(Categories,CategoriesAdmin)