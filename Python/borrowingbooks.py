#defines class with attributes of a title, author and allowing every book that is passed through this method to be available
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

#defines method to display details of the book and its availability
    def display_details (self):
        print(f"Title: {self.title}, Author: {self.author}, Availability: {'Available' if self.available else 'Not Available'}")

#defines class of library and defines a method in which will be take information about books
class Library:
    def __init__(self):
        self.books =[ ]

#defines a method which will add a book to the library
    def add_book(self, book):
        self.books.append(book)

#defines a method which will display whether there are books in the library or not
    def display_books(self):
        if not self.books:
            print("No books in the library, babe!")
        else:
            print("Books in the library!")
            for book in self.books: 
                book.display_details()

#defines a method which checks whether a book has been borrowed and provide an answer for 2 possible possibilities
    def borrow_book(self, title):
        for book in self.books:
           if book.title == title and book.available:
            book.available = False
            print(f"You have borrowed the book: {title}")
            return
        print(f"Book '{title}' not available for borrowing.")

#defines a method which checks whether a book has been returned and provide an answer for 2 possible possibilities
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You have returned the book: {title}")
                return
            print(f"Book '{title}' not marked as borrowed")
           
#Example Usage

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.display_books()
