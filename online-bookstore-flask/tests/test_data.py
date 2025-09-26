# pylint: disable=unnecessary-pass
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace
# 
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

# ---------- Unit Tests for BOOKS Data ----------
import unittest

class TestTestDataBooks(unittest.TestCase):
    """Unit test cases to validate the BOOKS test data array"""

    def test_books_list_not_empty(self):
        """Verify that BOOKS list contains book objects"""
        self.assertTrue(len(BOOKS) > 0, "BOOKS list should not be empty")

    def test_books_all_instances_of_book(self):
        """Verify all entries in BOOKS are instances of Book"""
        for book in BOOKS:
            self.assertIsInstance(book, Book, f"{book} is not an instance of Book")

    def test_books_have_valid_fields(self):
        """Verify each book has valid title, category, price, and image path"""
        for book in BOOKS:
            self.assertIsInstance(book.title, str)
            self.assertIsInstance(book.category, str)
            self.assertIsInstance(book.price, (float, int))
            self.assertGreater(book.price, 0)
            self.assertIsInstance(book.image, str)
            self.assertTrue(book.image.startswith("/images/books/"))

    def test_expected_books_titles_exist(self):
        """Verify expected titles are present in BOOKS"""
        expected_titles = {"The Great Gatsby", "1984", "I Ching", "Moby Dick"}
        actual_titles = {book.title for book in BOOKS}
        self.assertEqual(expected_titles, actual_titles)

if __name__ == "__main__":
    unittest.main()
