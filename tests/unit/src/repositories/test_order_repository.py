from src.models import Order
from src.repositories import OrderRepository
from unittest.mock import patch
import unittest


class TestOrderRepository(unittest.TestCase):
    @patch("src.repositories.order_repository.db")
    def test_create_order(self, db):
        order = Order()
        OrderRepository.create(order)
        self.assertIsNotNone(order.created_at)
        self.assertIsNotNone(order.updated_at)
        self.assertEqual(order.created_at, order.updated_at)
        db.session.add.assert_called_once_with(order)
        db.session.commit.assert_called_once()

    @patch("src.repositories.order_repository.Order")
    def test_get_all_orders(self, order_mock):
        mock_orders = [Order(), Order()]
        order_mock.query.all.return_value = mock_orders
        orders = OrderRepository.get_all()
        self.assertEqual(len(orders), 2)

    @patch("src.repositories.order_repository.Order")
    def test_get_by_id(self, order_mock):
        order_id = 1
        expected_order = Order()
        order_mock.query.get.return_value = expected_order
        order = OrderRepository.get_by_id(order_id)
        self.assertEqual(expected_order, order)
        order_mock.query.get.assert_called_once_with(order_id)
