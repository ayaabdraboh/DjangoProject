from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
#path('index/', views.index, name='index'),
    path('', views.index, name='index'),
     path('signup', views.signup, name='signup'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
     path('writers/', views.WriterListView.as_view(), name='writers'),
     path('writer/<int:pk>', views.WriterDetailView.as_view(), name='author-detail')
]
