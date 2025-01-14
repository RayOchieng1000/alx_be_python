# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True
    
    def return_book(self):
        """Return the book to the library."""
        if not self._is_checked_out:
            return False  # Book is not checked out
        self._is_checked_out = False
        return True
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages books."""
    
    def __init__(self):
        self._books = []  # private list to store books
    
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and book.check_out():
                return True
        return False  # Book not found or already checked out
    
    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and book.return_book():
                return True
        return False  # Book not found or not checked out
    
    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
