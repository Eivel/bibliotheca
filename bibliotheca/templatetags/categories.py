from django import template
from bibliotheca.models import Categories

register = template.Library()

@register.inclusion_tag('cat_menu.html')
def get_main_categories():
    main = Categories.objects.get(name='Książki')
    cats = Categories.objects.filter(top_category_id=main.id)
    return {'cats' : cats}