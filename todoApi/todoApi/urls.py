from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('todo/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
