"""
Reusable test data for unit tests across the Online Bookstore project.

This module defines a predefined list of Book instances used in multiple test modules,
such as test_cart.py, test_books.py, and others. It helps ensure consistent input
data across tests and reduces duplication.

Books included:
- The Great Gatsby (Fiction)
- 1984 (Dystopia)
- I Ching (Traditional)
- Moby Dick (Adventure)

This test data is aligned with the sample data used in the application itself
(app.py) and serves as a common fixture for validating cart and search functionality.
"""

from models import Book

BOOKS = [
    Book("The Great Gatsby", "Fiction", 10.99, "/images/books/the_great_gatsby.jpg"),
    Book("1984", "Dystopia", 8.99, "/images/books/1984.jpg"),
    Book("I Ching", "Traditional", 18.99, "/images/books/I-Ching.jpg"),
    Book("Moby Dick", "Adventure", 12.49, "/images/books/moby_dick.jpg")
]