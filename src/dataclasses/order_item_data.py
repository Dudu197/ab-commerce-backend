from dataclasses import dataclass
from src.models import OrderItem
from .product_data import ProductData


@dataclass
class OrderItemData:
    id: int
    product: ProductData
    quantity: int

    @staticmethod
    def from_order_item(order_item: OrderItem, product: ProductData) -> "OrderItemData":
        """
        Create an order item data from an order item

        Parameters
        ----------
        order_item: OrderItem
            The order item
        product: ProductData
            The product data

        Returns
        -------
        OrderItemData
            The order item data
        """
        return OrderItemData(
            id=order_item.id, product=product, quantity=order_item.quantity
        )
