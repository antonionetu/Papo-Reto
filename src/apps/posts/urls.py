from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name="post_list"),
    path('<int:id_post>', post_page, name="post_page"),
]
