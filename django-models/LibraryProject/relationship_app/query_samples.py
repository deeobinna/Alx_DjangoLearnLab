from relationship_app.models import Author, Book, Library, Librarian

#list all books in the library 
library_books = Library.objects.get(name = library_name)
    

#query all books by a specific author
author = Author.objects.get(name='J.K. Rowling')
    
#retrieve the librarian for a library
librarian = Librarian.objects.get(name='City Library')
    