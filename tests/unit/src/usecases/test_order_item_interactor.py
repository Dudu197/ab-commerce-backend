from src.usecases import OrderItemInteractor
from unittest.mock import patch
import unittest


class TestOrderItemInteractor(unittest.TestCase):
    @patch("src.usecases.order_item_interactor.OrderItemRepository")
    @patch("src.usecases.order_item_interactor.ProductRepository")
    def test_create(self, mock_product_repository, mock_order_item_repository):
        order_id = 1
        product_id = 2
        quantity = 3
        product = mock_product_repository.get_by_id.return_value

        result = OrderItemInteractor.create(order_id, product_id, quantity)

        self.assertEqual(result.product, product)
        self.assertEqual(result.quantity, quantity)

        mock_product_repository.get_by_id.assert_called_once_with(product_id)
        mock_order_item_repository.create.assert_called_once()
