from relationship_app.models import Author, Book, Library, Librarian

#list all books in the library 
books = Book.objects.all()

#query all books by a specific author
author = Author.objects.get(name='J.K. Rowling')
    
#retrieve the librarian for a library
librarian = Librarian.objects.get(name='City Library')
    