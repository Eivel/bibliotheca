from django.contrib import admin
from bibliotheca.models import *
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'creation_date', 'modification_date', 'text_body']

admin.site.register(News, NewsAdmin)
