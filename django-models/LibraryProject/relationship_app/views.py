from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book, Author

# Create your views here.
#list all books and their authors
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})
    
#Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
