"""
URL configuration for uniquest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
#from appquest import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    
    path('users/', include('appusers.urls')),
    path('questions/', include('appquest.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('apphome.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('ckeditor', include('ckeditor_uploader.urls')),
]
# configuração servidor local
#urlpatterns += staticfiles_urlpatterns()
# configuração Vercel
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)