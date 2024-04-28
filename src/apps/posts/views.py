import markdown

from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q

from .models import Post

from  .utils.slugs import generate


@require_http_methods(["GET"])
def post_list(request):
    query_search = request.GET['q'] if request.GET.get('q') else None

    post_data = get_list_or_404(
        Post.objects.order_by('-views', '-likes', '-created_at'), 
        Q(title__contains=query_search) if query_search else Q(),
    )

    return render(request, 'pages/posts/list.html', {
        'posts': post_data
    })


@require_http_methods(["GET"])
def post_page(request, post_slug):
    md = markdown.Markdown(extensions=["fenced_code"])

    post_data = get_object_or_404(Post, slug=post_slug)
    post_data.content = md.convert(post_data.content)

    return render(request, 'pages/posts/post.html', {
        'post': post_data
    })
