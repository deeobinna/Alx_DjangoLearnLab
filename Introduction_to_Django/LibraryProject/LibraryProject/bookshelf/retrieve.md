#to retrieve a book 

book = Book.objects.get(id=1)

print(book)

Output
Title 1984 by George Orwell