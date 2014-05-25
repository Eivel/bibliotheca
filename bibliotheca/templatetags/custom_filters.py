__author__ = 'Wojciech'
from django import template
from bibliotheca.models import Categories

register = template.Library()

def categories_list(format_string):
    cats = Categories.objects.all()
    return cats

register.simple_tag(categories_list)