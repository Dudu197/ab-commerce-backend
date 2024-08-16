from src.dataclasses import CartData, CartItemData, ProductData
from src.models import Cart
from datetime import datetime
import unittest


class TestCartData(unittest.TestCase):
    def test_from_cart(self):
        cart = Cart(
            id=1,
            user_id=1,
        )
        cart_item = CartItemData(
            cart_id=1,
            product_id=1,
            quantity=1,
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
        )
        cart_data = CartData.from_cart(cart, [cart_item])
        self.assertEqual(cart_data.user_id, cart.user_id)
        self.assertEqual(cart_data.items, [cart_item])
