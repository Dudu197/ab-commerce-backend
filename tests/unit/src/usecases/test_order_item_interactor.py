from datetime import datetime

from src.dataclasses import ProductData
from src.models import OrderItem
from src.usecases import OrderItemInteractor
from unittest.mock import patch
import unittest


class TestOrderItemInteractor(unittest.TestCase):
    @patch("src.usecases.order_item_interactor.OrderItemRepository")
    @patch("src.usecases.order_item_interactor.ProductInteractor")
    def test_create(self, mock_product_interactor, mock_order_item_repository):
        order_id = 1
        product_id = 2
        quantity = 3
        product_data = ProductData(
            id=product_id,
            name="test",
            price=10.0,
            description="test",
            category="test",
            image="test",
            stock=10,
            created_at=datetime.now(),
            deleted_at=datetime.now(),
        )
        mock_product_interactor.get_by_id.return_value = product_data
        order_item_data = OrderItemInteractor.create(order_id, product_id, quantity)

        self.assertEqual(order_item_data.product, product_data)
        mock_order_item_repository.create.assert_called_once()

    @patch("src.usecases.order_item_interactor.OrderItemRepository")
    @patch("src.usecases.order_item_interactor.ProductInteractor")
    def test_create_invalid_product(
        self, mock_product_interactor, mock_order_item_repository
    ):
        order_id = 1
        product_id = 2
        quantity = 3
        product_data = ProductData(
            id=product_id,
            name="test",
            price=10.0,
            description="test",
            category="test",
            image="test",
            stock=0,
            created_at=datetime.now(),
            deleted_at=datetime.now(),
        )
        mock_product_interactor.get_by_id.return_value = product_data

        with self.assertRaises(ValueError):
            OrderItemInteractor.create(order_id, product_id, quantity)

    @patch("src.usecases.order_item_interactor.OrderItemRepository")
    @patch("src.usecases.order_item_interactor.ProductInteractor")
    def test_create_invalid_quantity(
        self, mock_product_interactor, mock_order_item_repository
    ):
        order_id = 1
        product_id = 2
        quantity = 3
        product_data = ProductData(
            id=product_id,
            name="test",
            price=10.0,
            description="test",
            category="test",
            image="test",
            stock=1,
            created_at=datetime.now(),
            deleted_at=datetime.now(),
        )
        mock_product_interactor.get_by_id.return_value = product_data

        with self.assertRaises(ValueError):
            OrderItemInteractor.create(order_id, product_id, quantity)

    @patch("src.usecases.order_item_interactor.OrderItemRepository")
    @patch("src.usecases.order_item_interactor.ProductInteractor")
    def test_list_by_order_id(
        self, mock_product_interactor, mock_order_item_repository
    ):
        order_id = 1
        product_id = 2
        quantity = 3
        product_data = ProductData(
            id=product_id,
            name="test",
            price=10.0,
            description="test",
            category="test",
            image="test",
            stock=1,
            created_at=datetime.now(),
            deleted_at=datetime.now(),
        )
        mock_product_interactor.get_by_id.return_value = product_data
        order_item = OrderItem(
            order_id=order_id, product_id=product_id, quantity=quantity
        )
        mock_order_item_repository.list_by_order_id.return_value = [order_item]

        order_item_data = OrderItemInteractor.list_by_order_id(order_id)

        self.assertEqual(order_item_data[0].product, product_data)
        mock_order_item_repository.list_by_order_id.assert_called_once()
