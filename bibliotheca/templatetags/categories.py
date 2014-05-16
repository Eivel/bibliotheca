from django import template
from bibliotheca.models import Categories

register = template.Library()

@register.inclusion_tag('categories.html')
def get_main_categories():
    cats = Categories.objects.filter(is_main_category = True)
    return {'cats' : cats}