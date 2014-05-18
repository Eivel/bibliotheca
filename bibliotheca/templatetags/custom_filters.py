__author__ = 'Wojciech'
from django import template
from bibliotheca.models import Categories

register = template.Library()

@register.filter
def get_category_id(url):
    return url.rsplit('/',1)