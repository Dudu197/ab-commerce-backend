from src.models import CartItem
from src.dataclasses import CartItemData
from src.repositories import CartItemRepository
from .product_interactor import ProductInteractor


class CartItemInteractor:
    @staticmethod
    def add_item(cart_id: int, product_id: int, quantity: int) -> CartItemData:
        """
        Add an item to a cart

        Parameters
        ----------
        cart_id: int
            The cart's ID
        product_id: int
            The product's ID
        quantity: int
            The quantity

        Returns
        -------
        CartItemData
            The cart item data
        """
        cart_item = CartItemRepository.get_by_cart_and_product(cart_id, product_id)
        product = ProductInteractor.get_by_id(product_id)
        if cart_item is None:
            cart_item = CartItem(
                cart_id=cart_id, product_id=product_id, quantity=quantity
            )
            CartItemRepository.create(cart_item)
        else:
            cart_item.quantity += quantity
            CartItemRepository.update(cart_item)
        return CartItemData.from_cart_item(cart_item, product)

    @staticmethod
    def remove_item(cart_id: int, product_id: int):
        """
        Remove an item from a cart

        Parameters
        ----------
        cart_id: int
            The cart's ID
        product_id: int
            The product's ID
        """
        cart_item = CartItemRepository.get_by_cart_and_product(cart_id, product_id)
        if cart_item is not None:
            CartItemRepository.delete(cart_item)

    @staticmethod
    def update_item(cart_id: int, product_id: int, quantity: int) -> CartItemData:
        """
        Update an item in a cart

        Parameters
        ----------
        cart_id: int
            The cart's ID
        product_id: int
            The product's ID
        quantity: int
            The quantity

        Returns
        -------
        CartItemData
            The cart item data
        """
        cart_item = CartItemRepository.get_by_cart_and_product(cart_id, product_id)
        if cart_item is not None:
            cart_item.quantity = quantity
            CartItemRepository.update(cart_item)
            product = ProductInteractor.get_by_id(product_id)
            return CartItemData.from_cart_item(cart_item, product)
        return None

    @staticmethod
    def get_all_by_cart(cart_id: int) -> list[CartItemData]:
        """
        Get all cart items by cart ID

        Parameters
        ----------
        cart_id: int
            The cart's ID

        Returns
        -------
        List[CartItemData]
            The cart items data
        """
        cart_items = CartItemRepository.get_all_by_cart(cart_id)
        return [
            CartItemData.from_cart_item(
                cart_item, ProductInteractor.get_by_id(cart_item.product_id)
            )
            for cart_item in cart_items
        ]
