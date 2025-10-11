from library import Library
from book import Book

library  = Library()
book1 = Book("Python crash course:", "John", 2014)
book2 = Book("Java", "Chadwid", 1999)
library.add_books(book1)
library.add_books(book2)
library.display_books()