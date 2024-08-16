from src.models import CartItem
from .product_data import ProductData
from dataclasses import dataclass


@dataclass
class CartItemData:
    cart_id: int
    product_id: int
    quantity: int
    product: ProductData

    @staticmethod
    def from_cart_item(cart_item: CartItem, product: ProductData) -> "CartItemData":
        return CartItemData(
            cart_id=cart_item.cart_id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            product=product,
        )
