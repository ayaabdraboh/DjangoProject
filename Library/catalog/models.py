# from audioop import reverse
from django.urls import reverse

from django.db import models
from datetime import date

# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=200,
                            help_text="Enter a the country's natural language (e.g. Egypt, UK, French, etc.)")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publishedAt = models.DateField(null=True, blank=True)

    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")

    country =  models.CharField(max_length=200,
                            help_text="Enter a the country's natural language (e.g. Egypt, UK, French, etc.)")

    link = models.CharField(max_length=200, help_text="Enter a link of the book")
    author = models.ForeignKey('Writer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
          return reverse('book-detail', args=[str(self.id)])



class Writer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death= models.DateField('died', null=True, blank=True)
    contact = models.CharField(max_length=100)

    books = models.CharField(max_length=100, help_text="enter books here ")
    bio = models.ImageField(upload_to='pictures', blank=True)

    class Meta:
        ordering = ["first_name", "last_name"]

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}{1}'.format(self.first_name, self.last_name)
