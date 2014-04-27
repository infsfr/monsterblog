from django.shortcuts import render, get_object_or_404
from models import Tag
from posts.models import Post
from categories.models import Category


def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'posts.html', {
        'title': tag.name,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })
