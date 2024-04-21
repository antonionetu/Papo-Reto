from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.db.models import Q

from .models import Post


@require_http_methods(["GET"])
def post_list(request):
    query_search = request.GET['q'] if request.GET.get('q') else None
    # ...

    post_data = Post.objects.filter(
        Q(title__contains=query_search) if query_search else Q(),
        # ...
    ).order_by('-viewers_count', '-likes', '-created_at')

    return render(request, 'pages/posts/list.html', {
        'posts': post_data
    })


@require_http_methods(["GET"])
def post_page(request, id_post):
    post_data = Post.objects.get(id=id_post)
    return render(request, 'pages/posts/post.html', {
        'post': post_data
    })