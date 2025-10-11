# Project: Mini Library Management System

    # Features we can include:
    # Add a book – store book info (title, author, year).
    # Display all books – show the list of books.
    # Search a book – search by title.
    # Save & Load books – use a file so data persists.
    # OOP structure – use classes like Book and Library.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"{self.title} by {self.author} published in {self.year}")
#    __init__ : constructor used to create a book objecs
# info:method to print book details