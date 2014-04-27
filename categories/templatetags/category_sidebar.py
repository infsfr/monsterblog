from django import template
from categories.models import Category


register = template.Library()


@register.inclusion_tag('category_sidebar.html')
def show_category_sidebar():
    categories = Category.objects.all()
    return {'categories': categories}
