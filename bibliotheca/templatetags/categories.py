from django import template
from bibliotheca.models import Categories

register = template.Library()

@register.inclusion_tag('cat_menu.html')
def get_main_categories():
    main = Categories.objects.get(name='Książki')
    cats = Categories.objects.filter(top_category_id=main.id)
    return {'cats' : cats}

@register.inclusion_tag('search_categories_combobox.html')
def get_cats():
    cats = Categories.objects.all()
    return {'categories' : cats}