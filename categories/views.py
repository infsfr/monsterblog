from django.shortcuts import render, get_object_or_404
from models import Category
from posts.models import Post
from tags.models import Tag


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'posts.html', {
        'title': category.name,
        'category': category,
        'categories': categories,
        'posts': posts,
        'tags': tags,
    })
