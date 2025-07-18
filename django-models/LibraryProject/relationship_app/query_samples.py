from relationship_app.models import Author, Book, Library, Librarian

#list all books in the library 
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()
    

#query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.objects.filter(author=author)
    
#retrieve the librarian for a library
def get_librarian(library_name):
    library = Librarian.objects.get(library=library_name)
    return library.librarian