from src.models import CartItem
from src.repositories import CartItemRepository
from unittest.mock import patch
import unittest


class TestCartItemRepository(unittest.TestCase):
    @patch("src.repositories.cart_item_repository.db")
    def test_create_cart_item(self, db):
        cart_item = CartItem(cart_id=1, product_id=1, quantity=1)
        CartItemRepository.create(cart_item)
        db.session.add.assert_called_once_with(cart_item)
        db.session.commit.assert_called_once()

    @patch("src.repositories.cart_item_repository.CartItem")
    def test_get_all_cart_items(self, cart_item_mock):
        mock_cart_items = [CartItem(), CartItem()]
        cart_item_mock.query.filter_by.return_value.all.return_value = mock_cart_items
        cart_items = CartItemRepository.get_all_by_cart(1)
        self.assertEqual(len(cart_items), 2)
        cart_item_mock.query.filter_by.assert_called_once_with(cart_id=1)

    @patch("src.repositories.cart_item_repository.CartItem")
    def test_get_by_id(self, cart_item_mock):
        cart_item_id = 1
        expected_cart_item = CartItem()
        cart_item_mock.query.get.return_value = expected_cart_item
        cart_item = CartItemRepository.get_by_id(cart_item_id)
        self.assertEqual(expected_cart_item, cart_item)
        cart_item_mock.query.get.assert_called_once_with(cart_item_id)

    @patch("src.repositories.cart_item_repository.db")
    def test_delete_cart_item(self, db):
        cart_item = CartItem()
        CartItemRepository.delete(cart_item)
        db.session.delete.assert_called_once_with(cart_item)
        db.session.commit.assert_called_once()
