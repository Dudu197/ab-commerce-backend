from src.models import Cart
from src.usecases import CartInteractor
from unittest.mock import patch
import unittest


class TestCartInteractor(unittest.TestCase):

    @patch("src.usecases.cart_interactor.CartRepository")
    def test_create(self, cart_repository_mock):
        user_id = 1
        cart = Cart(user_id=user_id)
        cart_repository_mock.create.return_value = cart

        CartInteractor.create(user_id)

        cart_repository_mock.create.assert_called_once()

    @patch("src.usecases.cart_interactor.CartRepository")
    @patch("src.usecases.cart_interactor.CartItemInteractor")
    def test_get_by_user_id(self, cart_item_interactor_mock, cart_repository_mock):
        user_id = 1
        cart = Cart(id=1, user_id=user_id)
        cart_repository_mock.get_by_user_id.return_value = cart

        result = CartInteractor.get_by_user_id(user_id)

        self.assertEqual(result.user_id, user_id)
        cart_repository_mock.get_by_user_id.assert_called_with(user_id)
        cart_item_interactor_mock.get_all_by_cart.assert_called_with(cart.id)

    @patch("src.usecases.cart_interactor.CartRepository")
    def test_clean(self, cart_repository_mock):
        user_id = 1

        CartInteractor.clean(user_id)

        cart_repository_mock.clean.assert_called_with(user_id)

    @patch("src.usecases.cart_interactor.CartRepository")
    @patch("src.usecases.cart_interactor.CartItemInteractor")
    def test_add_item(self, cart_item_interactor_mock, cart_repository_mock):
        user_id = 1
        product_id = 2
        quantity = 3
        cart = Cart(id=1, user_id=user_id)
        cart_repository_mock.get_by_user_id.return_value = cart

        CartInteractor.add_item(user_id, product_id, quantity)

        cart_repository_mock.get_by_user_id.assert_called_with(user_id)
        cart_item_interactor_mock.add_item.assert_called_with(
            user_id, product_id, quantity
        )
