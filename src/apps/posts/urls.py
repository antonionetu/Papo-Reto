from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<str:post_slug>', post_page, name="post_page"),
]
