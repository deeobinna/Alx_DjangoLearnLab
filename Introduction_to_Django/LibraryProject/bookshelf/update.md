book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

Output
No output from .save(), but confirmed with:

python
print(book)
Title Nineteen Eighty-Four by George Orwell