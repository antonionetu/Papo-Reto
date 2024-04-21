from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id_post>', post_page, name="post_page"),
]
