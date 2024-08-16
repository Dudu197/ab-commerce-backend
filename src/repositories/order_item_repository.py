from src.models import OrderItem, db


class OrderItemRepository:
    @staticmethod
    def create(order_item: OrderItem):
        """
        Create a new order item

        Parameters
        ----------
        order_item: OrderItem
            The order item to be created
        """
        db.session.add(order_item)
        db.session.commit()

    @staticmethod
    def list_by_order_id(order_id: int) -> list[OrderItem]:
        """
        List order items by order ID

        Parameters
        ----------
        order_id: int
            The order's ID

        Returns
        -------
        list[OrderItem]
            The list of order items
        """
        return OrderItem.query.filter_by(order_id=order_id).all()
