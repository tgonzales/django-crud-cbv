from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Book, Author

class BooksListView(ListView):
    model = Book

class BooksCreateView(CreateView):
    model = Book
    success_url = reverse_lazy('livros') 

class BooksDetailView(DetailView):
    model = Book

class BooksUpdateView(UpdateView):
    model = Book
    success_url = reverse_lazy('livros')

class BooksDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('livros') 

class AuthorCreateView(CreateView):
    model = Author
    success_url = reverse_lazy('livros') 
