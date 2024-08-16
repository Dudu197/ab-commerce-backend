from dataclasses import dataclass
from .cart_item_data import CartItemData
from src.models import Cart


@dataclass
class CartData:
    user_id: int
    items: list[CartItemData]

    @staticmethod
    def from_cart(cart: Cart, items: [CartItemData]) -> "CartData":
        return CartData(
            user_id=cart.user_id,
            items=items,
        )
