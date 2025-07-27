from bookshelf.models import Book
#to delete a book
book = Book.objects.get(id=2)
book.delete()


Final Check
python
 print(Book.objects.all()) 
<QuerySet [<Book: Title Nineteen Eighty-Four by George Orwell>]