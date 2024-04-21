from django.shortcuts import render
from .models import Post


def post(request, id_post):
    post_data = Post.objects.get(id=id_post)
    print(post_data, id_post)
    return render(request, 'pages/index.html', {
        'post': post_data
    })