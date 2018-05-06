from django.contrib import admin
from .models import Writer, Book
# Register your models here.

@admin.register(Writer)
class WriterModel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death','contact','books','bio')
    fields = ['first_name', 'last_name','date_of_birth', 'date_of_death','contact','books','bio']
@admin.register(Book)
class BookModel(admin.ModelAdmin):

    list_display = ('title', 'publishedAt','country','author')
