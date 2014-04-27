from django import template
from tags.models import Tag


register = template.Library()


@register.inclusion_tag('tag_sidebar.html')
def show_tag_sidebar():
    tags = Tag.objects.all()
    return {'tags': tags}
