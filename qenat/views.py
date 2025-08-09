from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from qenat.models import Article, Book, Award, Photo, Contact
from itertools import chain

# Create your views here.
def home(request):
    news = sorted(
        chain(Article.objects.all(),
              Book.objects.all(),
              Award.objects.all(),
              Photo.objects.all()),
        key=lambda x: x.date,
        reverse=True,
    )
    context = {'news': news}
    return render(request, 'qenat/home.html', context=context)

def articles(request):
    articles = Article.objects.all().order_by('-date')
    context = {
        'articles': articles
    }
    return render(request, 'qenat/articles.html', context=context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'qenat/article.html', context=context)

def books(request):
    books = Book.objects.all().order_by('-date')
    context = {
        'books': books
    }
    return render(request, 'qenat/books.html', context=context)

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, 'qenat/book.html', context=context)

def gallery(request):
    gallery = Photo.objects.all().order_by('-date')
    context = {
        'gallery': gallery
    }
    return render(request, 'qenat/gallery.html', context=context)

def photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    context = {'photo': photo}
    return render(request, 'qenat/photo.html', context=context)

def awards(request):
    awards = Award.objects.all().order_by('-date')
    context = {
        'awards': awards
    }
    return render(request, 'qenat/awards.html', context=context)

def award(request, award_id):
    award = Award.objects.get(id=award_id)
    context = {'award': award}
    return render(request, 'qenat/award.html', context=context)

def contacts(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'qenat/contacts.html', context=context)

def error_404(request, exception):
    return render(request, 'qenat/404.html')

def error_500(request):
    return render(request, 'qenat/500.html')