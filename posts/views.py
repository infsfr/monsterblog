from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from models import Post


def index(request, page_number=1):
    posts = Post.objects.all()
    current_page = Paginator(posts, 5)
    return render(request, 'posts.html', {
        'posts': current_page.page(page_number),
    })


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if not request.session.exists('has_viewed_'+str(post.id)):
        post.views_count += 1
        post.save
        request.session['has_viewed_'+str(post.id)] = True

    try:
        prev_post = post.get_previous_by_created_at()
    except:
        prev_post = False
    try:
        next_post = post.get_next_by_created_at()
    except:
        next_post = False
    return render(request, 'post.html', {
        'title': post.title,
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
    })


# def add_like(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     post.likes += 1
#     post.save()
#     return redirect('/')
