from dataclasses import dataclass
from datetime import datetime
from src.dataclasses import OrderItemData
from src.models import Order


@dataclass
class OrderData:
    id: int
    total: float
    items: list[OrderItemData]
    status: str
    created_at: datetime

    @staticmethod
    def from_order(order: Order, order_items: list[OrderItemData]) -> "OrderData":
        """
        Create an order data from an order

        Parameters
        ----------
        order: Order
            The order
        order_items: list[OrderItemData]
            The list of order items

        Returns
        -------
        OrderData
            The order data
        """
        return OrderData(
            id=order.id,
            total=order.total,
            items=order_items,
            status=order.status,
            created_at=order.created_at,
        )
