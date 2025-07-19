from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book, Author

# Create your views here.
#list all books and their authors
def list_books(request):
    books = Book.objects.all()
    for book in books:
        return render(request, 'relationship_app/list_books.html', {'books': books.title, 'author': book.author.name})
    
#Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context  