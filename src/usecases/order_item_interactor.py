from src.models import OrderItem
from src.dataclasses import OrderItemData
from src.repositories import OrderItemRepository
from .product_interactor import ProductInteractor


class OrderItemInteractor:
    @classmethod
    def create(cls, order_id: int, product_id: int, quantity: int) -> OrderItemData:
        """
        Create a new order item

        Parameters
        ----------
        order_id: int
            The order's ID
        product_id: int
            The product's ID
        quantity: int
            The quantity

        Returns
        -------
        OrderItemData
            The order item data

        Raises
        -------
        ValueError
            If the order item is invalid
        """
        order_item = OrderItem(
            order_id=order_id, product_id=product_id, quantity=quantity
        )
        product = ProductInteractor.get_by_id(product_id)
        cls.__validate_order_item_attributes(order_item)
        OrderItemRepository.create(order_item)
        return OrderItemData.from_order_item(order_item, product)

    @classmethod
    def list_by_order_id(cls, order_id: int) -> list[OrderItemData]:
        """
        List order items by order ID

        Parameters
        ----------
        order_id: int
            The order's ID

        Returns
        -------
        list[OrderItemData]
            The list of order item data
        """
        order_items = OrderItemRepository.list_by_order_id(order_id)
        return [
            OrderItemData.from_order_item(
                order_item, ProductInteractor.get_by_id(order_item.product_id)
            )
            for order_item in order_items
        ]

    @classmethod
    def __validate_order_item_attributes(cls, order_item: OrderItem):
        """
        Validate order item attributes

        Parameters
        ----------
        order_item: OrderItem

        Raises
        -------
        ValueError
            If the order item is invalid
        """
        if order_item.quantity is None or order_item.quantity <= 0:
            raise ValueError("The quantity must be greater than 0")
        product = ProductInteractor.get_by_id(order_item.product_id)
        if product is None:
            raise ValueError("The product does not exist")
        if product.stock < order_item.quantity:
            raise ValueError("The product is out of stock")
