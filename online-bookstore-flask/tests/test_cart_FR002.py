# pylint: disable=unnecessary-pass
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

"""
Unit tests for shopping cart functionality (FR-002).

This module verifies:
- Adding books to the cart.
- Updating item quantities.
- Removing individual items and clearing the cart.
- Dynamic recalculation of the cart total.

These tests ensure that cart operations behave as expected according to FR-002.
"""

import unittest
from tests.test_data import BOOKS
from models import Cart

class TestShoppingCart(unittest.TestCase):

    """Unit test cases for FR-002: Shopping cart functionality"""

    def setUp(self):
        self.test_cart = Cart()

    def test_add_book_to_cart(self):
        """FR002-01: Test adding a book to the cart"""
        self.test_cart.add_book(BOOKS[1], 1)
        self.assertEqual(len(self.test_cart.items), 1)
        self.assertEqual(self.test_cart.get_total_price(), BOOKS[1].price)

    def test_update_book_quantity(self):
        """FR002-02: Test updating the quantity of a book in the cart"""
        self.test_cart.add_book(BOOKS[1], 1)
        self.test_cart.update_quantity(BOOKS[1].title, 2)
        self.assertEqual(self.test_cart.get_total_items(), 2)
        self.assertEqual(len(self.test_cart.items), 1)

    def test_remove_book_from_cart(self):
        """FR002-03: Test removing a book from the cart"""
        self.test_cart.add_book(BOOKS[1], 1)
        self.test_cart.remove_book(BOOKS[1].title)
        self.assertEqual(len(self.test_cart.items), 0)
        self.assertEqual(self.test_cart.get_total_price(), 0)
    
    def test_clear_cart(self):
        """FR002-04: Test clearing all items from the cart"""
        self.test_cart.add_book(BOOKS[0], 1)
        self.test_cart.add_book(BOOKS[1], 2)
        self.test_cart.clear()
        self.assertEqual(len(self.test_cart.items), 0)
        self.assertEqual(self.test_cart.get_total_price(), 0)

    def test_total_price_calculation_for_multiple_books(self):
        """FR002-05: Test total price calculation for multiple books"""
        self.test_cart.add_book(BOOKS[0], 2)  # $10.99 × 2
        self.test_cart.add_book(BOOKS[3], 1)  # $12.49
        expected_total = (BOOKS[0].price * 2) + BOOKS[3].price
        self.assertAlmostEqual(self.test_cart.get_total_price(), expected_total, places=2)

    def test_total_price_updates_when_item_removed(self):
        """FR002-06: Test total price updates when an item is removed"""
        self.test_cart.add_book(BOOKS[0], 1)
        self.test_cart.add_book(BOOKS[1], 1)
        self.test_cart.remove_book(BOOKS[1].title)
        self.assertAlmostEqual(self.test_cart.get_total_price(), BOOKS[0].price, places=2)

    def test_removing_book_not_in_cart_does_nothing(self):
        """FR002-07: Test removing a book not in the cart does nothing"""
        self.test_cart.add_book(BOOKS[2], 1)
        self.test_cart.remove_book("Nonexistent Book")
        self.assertEqual(len(self.test_cart.items), 1)
        self.assertAlmostEqual(self.test_cart.get_total_price(), BOOKS[2].price, places=2)

    def test_update_quantity_to_zero_removes_book(self):
        """FR002-08 / FR002-09: Test updating quantity to 0 removes book from cart"""
        self.test_cart.add_book(BOOKS[3], 1)
        self.test_cart.update_quantity(BOOKS[3].title, 0)
        self.assertEqual(len(self.test_cart.items), 0)
        self.assertEqual(self.test_cart.get_total_price(), 0)

if __name__ == "__main__":
    unittest.main()
