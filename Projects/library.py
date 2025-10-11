import book

class Library:
    def __init__(self):
         self.books = []     #this will store all book objects
    
    def add_books(self, book):
        self.books.append(book)
    
    def display_books(self):
        if not self.books:
            print("No book in the library yet!")
        for book in self.books:
            # print(f"{book.title} by {book.author}, {book.year}")
            book.info()

# self.books → list to store Book objects.
# add_book(book) → adds a Book object to the library.
# display_books() → prints info for all books.