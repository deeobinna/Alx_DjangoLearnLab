#New Book creation
new_book = Book.objects.create(title="1984",author="George Orwell",publication_year=1949)


#to save
new_book.save()

#Output
No output from .save(), but creation is confirmed by:

python
new_book = Book.objects.values_list()
# Output:
#[(1, 'Nineteen Eighty-Four', 'George Orwell', 1949), (2, 'Things Fall Apart', 'Chinua Achebe', 1994)]>