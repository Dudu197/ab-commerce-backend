from src.models import OrderItem
from src.repositories import OrderItemRepository
from unittest.mock import patch
import unittest


class TestCartItemRepository(unittest.TestCase):
    @patch("src.repositories.order_item_repository.db")
    def test_create_cart_item(self, db):
        cart_item = OrderItem(order_id=1, product_id=1, quantity=1)
        OrderItemRepository.create(cart_item)
        db.session.add.assert_called_once_with(cart_item)
        db.session.commit.assert_called_once()
