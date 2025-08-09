"""
URL configuration for qenat_project project.

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
from cgitb import handler

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from qenat import views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:article_id>', views.article, name='article') ,
    path('books/', views.books, name='books'),
    path('book/<int:book_id>', views.book, name='book'),
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<int:photo_id>', views.photo, name='photo'),
    path('awards/', views.awards, name='awards'),
    path('award/<int:award_id>', views.award, name='award'),
    path('contacts/', views.contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'qenat.views.error_404'
handler500 = 'qenat.views.error_500'