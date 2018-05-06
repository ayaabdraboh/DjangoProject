from django.shortcuts import render
from .models import Book, Writer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic




def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count(),
    num_writers=Writer.objects.count()  
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'catalog/index.html',
       # {'catalog':index}

       context={'num_books':num_books,'num_writers':num_writers},
    )
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/signup.html', {'form': form})

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all()[:5] # Get 5 books containing the title war    template_name = 'books/book_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book

class WriterListView(generic.ListView):
    model = Writer
    context_object_name = 'writer_list'   # your own name for the list as a template variable
    queryset = Writer.objects.all()[:5] # Get 5 books containing the title war    template_name = 'books/book_list.html'  # Specify your own template name/location
class WriterDetailView(generic.DetailView):
    model = Writer
