from datetime import datetime

from src.usecases.order_interactor import OrderInteractor
from src.dataclasses import (
    CartData,
    CartItemData,
    OrderData,
    OrderItemData,
    ProductData,
)
from src.models import Order
from unittest.mock import patch
import unittest


class TestOrderInteractor(unittest.TestCase):
    @patch("src.usecases.order_interactor.OrderRepository")
    @patch("src.usecases.order_interactor.CartInteractor")
    @patch("src.usecases.order_interactor.OrderItemInteractor")
    def test_create(
        self, mock_order_item_interactor, mock_cart_interactor, mock_order_repository
    ):
        user_id = 1
        order_id = 2
        order = Order(id=order_id)
        mock_order_repository.create.return_value = order
        product_data = ProductData(
            id=1,
            name="test",
            price=10.0,
            description="test",
            category="test",
            image="test",
            stock=1,
            created_at=datetime.now(),
            deleted_at=datetime.now(),
        )
        mock_cart_interactor.get_by_user_id.return_value = CartData(
            user_id=user_id,
            items=[
                CartItemData(cart_id=1, product_id=1, quantity=2, product=product_data)
            ],
        )

        order_data = OrderInteractor.create(user_id)

        self.assertEqual(order_data.total, 20)

        mock_order_item_interactor.create.assert_called_once_with(None, 1, 2)
        mock_cart_interactor.clean.assert_called_once_with(user_id)

    @patch("src.usecases.order_interactor.OrderRepository")
    @patch("src.usecases.order_interactor.OrderItemInteractor")
    def test_list_by_user_id(self, mock_order_item_interactor, mock_order_repository):
        user_id = 1
        order_id = 2
        order = Order(id=order_id)
        mock_order_repository.list_by_user_id.return_value = [order]
        mock_order_item_interactor.list_by_order_id.return_value = [
            {"product_id": 1, "quantity": 2}
        ]

        order_data = OrderInteractor.list_by_user_id(user_id)
        
        self.assertEqual(order_data[0].id, order_id)
        mock_order_item_interactor.list_by_order_id.assert_called_once_with(order_id)
