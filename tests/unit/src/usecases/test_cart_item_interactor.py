from src.models import CartItem
from src.usecases.cart_item_interactor import CartItemInteractor
from unittest.mock import patch
import unittest


class TestCartItemInteractor(unittest.TestCase):

    @patch("src.usecases.cart_item_interactor.CartItemRepository")
    @patch("src.usecases.cart_item_interactor.ProductInteractor")
    def test_add_item(self, product_interactor_mock, cart_item_repository_mock):
        cart_id = 1
        product_id = 2
        quantity = 3
        product = "product"
        product_interactor_mock.get_by_id.return_value = product
        cart_item_repository_mock.get_by_cart_and_product.return_value = None

        cart_item_data = CartItemInteractor.add_item(cart_id, product_id, quantity)

        self.assertEqual(cart_item_data.cart_id, cart_id)
        self.assertEqual(cart_item_data.product_id, product_id)
        self.assertEqual(cart_item_data.quantity, quantity)
        self.assertEqual(cart_item_data.product, product)
        cart_item_repository_mock.get_by_cart_and_product.assert_called_with(
            cart_id, product_id
        )
        product_interactor_mock.get_by_id.assert_called_with(product_id)

    @patch("src.usecases.cart_item_interactor.CartItemRepository")
    @patch("src.usecases.cart_item_interactor.ProductInteractor")
    def test_add_item_with_previous_item(
        self, product_interactor_mock, cart_item_repository_mock
    ):
        cart_id = 1
        product_id = 2
        quantity = 3
        expected_quantity = 6
        product = "product"
        cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
        product_interactor_mock.get_by_id.return_value = product
        cart_item_repository_mock.get_by_cart_and_product.return_value = cart_item

        cart_item_data = CartItemInteractor.add_item(cart_id, product_id, quantity)

        self.assertEqual(cart_item_data.cart_id, cart_id)
        self.assertEqual(cart_item_data.product_id, product_id)
        self.assertEqual(cart_item_data.quantity, expected_quantity)
        self.assertEqual(cart_item_data.product, product)
        cart_item_repository_mock.get_by_cart_and_product.assert_called_with(
            cart_id, product_id
        )
        product_interactor_mock.get_by_id.assert_called_with(product_id)

    @patch("src.usecases.cart_item_interactor.CartItemRepository")
    def test_remove_item(self, cart_item_repository_mock):
        cart_id = 1
        product_id = 2
        cart_item_repository_mock.get_by_cart_and_product.return_value = "cart_item"

        CartItemInteractor.remove_item(cart_id, product_id)

        cart_item_repository_mock.get_by_cart_and_product.assert_called_with(
            cart_id, product_id
        )
        cart_item_repository_mock.delete.assert_called_with("cart_item")

    @patch("src.usecases.cart_item_interactor.CartItemRepository")
    def test_remove_item_not_found(self, cart_item_repository_mock):
        cart_id = 1
        product_id = 2
        cart_item_repository_mock.get_by_cart_and_product.return_value = None

        CartItemInteractor.remove_item(cart_id, product_id)

        cart_item_repository_mock.get_by_cart_and_product.assert_called_with(
            cart_id, product_id
        )
        cart_item_repository_mock.delete.assert_not_called()

    @patch("src.usecases.cart_item_interactor.CartItemRepository")
    @patch("src.usecases.cart_item_interactor.ProductInteractor")
    def test_update_item(self, product_interactor_mock, cart_item_repository_mock):
        cart_id = 1
        product_id = 2
        quantity = 3
        product = "product"
        product_interactor_mock.get_by_id.return_value = product
        cart_item_repository_mock.get_by_cart_and_product.return_value = CartItem(
            cart_id=cart_id, product_id=product_id, quantity=quantity
        )

        cart_item_data = CartItemInteractor.update_item(cart_id, product_id, quantity)

        self.assertEqual(cart_item_data.cart_id, cart_id)
        self.assertEqual(cart_item_data.product_id, product_id)
        self.assertEqual(cart_item_data.quantity, quantity)
        self.assertEqual(cart_item_data.product, product)
        cart_item_repository_mock.get_by_cart_and_product.assert_called_with(
            cart_id, product_id
        )
        product_interactor_mock.get_by_id.assert_called_with(product_id)
