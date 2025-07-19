from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    #query all books by a specific author
    author = Author.objects.get(name='J.K. Rowling')
    
    #get all books in the library   
    books = Library.objects.get(name = "library_name").books.all()
    
    #retrieve the librarian for a library
    librarian = Librarian.objects.get(name='City Library')
    