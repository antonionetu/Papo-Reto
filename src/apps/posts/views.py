from django.shortcuts import render
from .models import Post


def post_page(request, id_post):
    post_data = Post.objects.get(id=id_post)
    return render(request, 'pages/post.html', {
        'post': post_data
    })