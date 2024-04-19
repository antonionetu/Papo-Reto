from django.shortcuts import render


def post(request, id_post):    
    return render(request, 'pages/index.html', {
        'id_post': id_post,
        'title': 'Um post legal!'
    })