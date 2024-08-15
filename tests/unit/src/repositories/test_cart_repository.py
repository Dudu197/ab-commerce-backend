from src.models import Cart
from src.repositories import CartRepository
from unittest.mock import patch
import unittest


class TestCartRepository(unittest.TestCase):
    @patch("src.repositories.cart_repository.db")
    def test_create_cart(self, db):
        cart = Cart()
        CartRepository.create(cart)
        db.session.add.assert_called_once_with(cart)
        db.session.commit.assert_called_once()

    @patch("src.repositories.cart_repository.Cart")
    def test_get_by_user_id(self, cart_mock):
        user_id = 1
        expected_cart = Cart()
        cart_mock.query.get.return_value = expected_cart
        cart = CartRepository.get_by_user_id(user_id)
        self.assertEqual(expected_cart, cart)
        cart_mock.query.get.assert_called_once_with(user_id)

    @patch("src.repositories.cart_repository.Cart")
    @patch("src.repositories.cart_repository.CartItemRepository")
    def test_clean_cart(self, cart_item_repository_mock, cart_mock):
        user_id = 1
        cart = Cart()
        cart_mock.query.get.return_value = cart
        cart_item_repository_mock.get_all_by_cart.return_value = [1, 2, 3]
        CartRepository.clean(user_id)
        cart_mock.query.get.assert_called_once_with(user_id)
        cart_item_repository_mock.get_all_by_cart.assert_called_once_with(cart.id)
        self.assertEqual(cart_item_repository_mock.delete.call_count, 3)
        self.assertEqual(
            cart_item_repository_mock.delete.call_args_list, [((1,),), ((2,),), ((3,),)]
        )
