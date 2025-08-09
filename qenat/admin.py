from django.contrib import admin
from qenat.models import Article, Book, Photo, Award, Contact

# Register your models here.
admin.site.register(Article)
admin.site.register(Book)
admin.site.register(Photo)
admin.site.register(Award)
admin.site.register(Contact)