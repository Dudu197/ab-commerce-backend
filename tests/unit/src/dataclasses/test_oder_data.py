from datetime import datetime

from src.dataclasses import OrderData, OrderItemData, ProductData
from src.models import Order
import unittest


class TestOrderData(unittest.TestCase):
    def test_from_order(self):
        order = Order(
            id=1,
            user_id=1,
            total=10.0,
            status="pending",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        order_item = OrderItemData(
            id=1,
            product=ProductData(
                id=1,
                name="product",
                price=10.0,
                description="description",
                category="category",
                image="image",
                stock=10,
                created_at=datetime.now(),
                deleted_at=None,
            ),
            quantity=1,
        )
        order_data = OrderData.from_order(order, [order_item])
        self.assertEqual(order_data.id, order.id)
        self.assertEqual(order_data.total, order.total)
        self.assertEqual(order_data.status, order.status)
        self.assertEqual(order_data.created_at, order.created_at)
        self.assertEqual(order_data.items, [order_item])
