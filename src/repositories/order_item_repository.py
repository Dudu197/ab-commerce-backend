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
