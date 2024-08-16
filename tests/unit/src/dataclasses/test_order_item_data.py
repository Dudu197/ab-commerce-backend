from datetime import datetime

from src.dataclasses import OrderItemData, ProductData
from src.models import OrderItem
import unittest


class TestOrderItemData(unittest.TestCase):
    def test_from_order_item(self):
        order_item = OrderItem(
            id=1,
            order_id=1,
            product_id=1,
            quantity=1,
        )
        product = ProductData(
            id=1,
            name="product",
            price=10.0,
            description="description",
            category="category",
            image="image",
            stock=10,
            created_at=datetime.now(),
            deleted_at=None,
        )
        order_item_data = OrderItemData.from_order_item(order_item, product)
        self.assertEqual(order_item_data.id, order_item.id)
        self.assertEqual(order_item_data.quantity, order_item.quantity)
        self.assertEqual(order_item_data.product, product)
