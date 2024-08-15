from datetime import datetime

from src.models import Order, db


class OrderRepository:
    @staticmethod
    def create(order: Order):
        """
        Create a new order

        Parameters
        ----------
        order: Order
            The order to be created
        """
        now = datetime.now()
        order.created_at = now
        order.updated_at = now
        db.session.add(order)
        db.session.commit()

    @staticmethod
    def get_all() -> list[Order]:
        """
        Get all orders

        Returns
        -------
        list[Order]
            The list of orders
        """
        return Order.query.all()

    @staticmethod
    def get_by_id(order_id: int) -> Order:
        """
        Get an order by ID

        Parameters
        ----------
        order_id: int
            The order's ID

        Returns
        -------
        Order
            The order
        """
        return Order.query.get(order_id)
