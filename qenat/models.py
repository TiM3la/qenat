from django.db import models

# Create your models here.
class Article(models.Model):
    image = models.ImageField(upload_to='qenat/images/')
    file = models.FileField(upload_to='qenat/files/')
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    url = models.URLField(blank=True)
    date = models.DateField()
    def __str__(self):
        return f'{self.type} "{self.title}"'

    def type_(self):
        return self._meta.model_name

    class Meta:
        verbose_name_plural = 'Труд'

class Book(models.Model):
    image = models.ImageField(upload_to='qenat/images/')
    file = models.FileField(upload_to='qenat/files/')

    title = models.CharField(max_length=500)
    url = models.URLField(blank=True)
    date = models.DateField()
    def __str__(self):
        return f'Сборник "{self.title}"'

    def type_(self):
        return self._meta.model_name

    class Meta:
        verbose_name_plural = 'Cборник'

class Award(models.Model):
    image = models.ImageField(upload_to='qenat/images/')


    title = models.CharField(max_length=500)

    date = models.DateField()
    def __str__(self):
        return f'Достижение "{self.title}"'

    def type_(self):
        return self._meta.model_name

    class Meta:
        verbose_name_plural = 'Достижение'

class Photo(models.Model):
    image = models.ImageField(upload_to='qenat/images/')


    title = models.CharField(max_length=500)

    date = models.DateField()
    def __str__(self):
        return f'Фото "{self.title}"'

    def type_(self):
        return self._meta.model_name

    class Meta:
        verbose_name_plural = 'Фото'

class Contact(models.Model):
    image = models.ImageField(upload_to='qenat/images/')


    title = models.CharField(max_length=500)
    url = models.URLField(blank=True)
    tag = models.CharField(max_length=300)
    def __str__(self):
        return f'Контакт {self.title}'

    class Meta:
        verbose_name_plural = 'Контакт'


