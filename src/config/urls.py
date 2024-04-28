from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', RedirectView.as_view(url='/posts/', permanent=True)),
    path('posts/', include('apps.posts.urls'))
]
