from django.shortcuts import render
from .models import Book, Author

# Create your views here.
#list all books and their authors
def book_list(request):
    books = Book.objects.all()
    Author = Author.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books, 'authors': Author})