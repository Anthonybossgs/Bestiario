from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bestiaApp.views import base
from bestiaApp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name="base"),
    path('register/', views.register_user, name='register'), 
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
