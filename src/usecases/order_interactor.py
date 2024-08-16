from src.models import Order
from src.dataclasses import OrderData
from src.usecases import OrderItemInteractor, CartInteractor
from src.repositories import OrderRepository


class OrderInteractor:
    @staticmethod
    def create(user_id: int) -> OrderData:
        """
        Create a new order

        Parameters
        ----------
        user_id: int
            The user's ID

        Returns
        -------
        OrderData
            The order data
        """
        order = Order(user_id=user_id)
        cart = CartInteractor.get_by_user_id(user_id)
        order.total = sum(
            [cart_item.product.price * cart_item.quantity for cart_item in cart.items]
        )
        OrderRepository.create(order)
        for cart_item in cart.items:
            OrderItemInteractor.create(
                order.id, cart_item.product_id, cart_item.quantity
            )
        CartInteractor.clean(user_id)
        return OrderData.from_order(
            order, OrderItemInteractor.list_by_order_id(order.id)
        )

    @staticmethod
    def list_by_user_id(user_id: int) -> list[OrderData]:
        """
        List orders by user ID

        Parameters
        ----------
        user_id: int
            The user's ID

        Returns
        -------
        list[OrderData]
            The list of order data
        """
        orders = OrderRepository.list_by_user_id(user_id)
        return [
            OrderData.from_order(order, OrderItemInteractor.list_by_order_id(order.id))
            for order in orders
        ]
