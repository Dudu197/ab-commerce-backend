from datetime import datetime

from src.dataclasses import CartItemData, ProductData
from src.models import CartItem
import unittest


class TestCartItemData(unittest.TestCase):
    def test_from_cart_item(self):
        cart_item = CartItem(
            id=1,
            cart_id=1,
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
        cart_item_data = CartItemData.from_cart_item(cart_item, product)
        self.assertEqual(cart_item_data.quantity, cart_item.quantity)
        self.assertEqual(cart_item_data.product.id, cart_item.product_id)
        self.assertEqual(cart_item_data.cart_id, cart_item.cart_id)
        self.assertEqual(cart_item_data.product_id, cart_item.product_id)
