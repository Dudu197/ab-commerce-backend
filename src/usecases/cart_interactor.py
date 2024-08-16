from src.models import Cart
from src.dataclasses import CartData
from src.repositories import CartRepository
from src.usecases import CartItemInteractor


class CartInteractor:
    @staticmethod
    def create(user_id: int) -> CartData:
        """
        Create a new cart

        Parameters
        ----------
        user_id: int
            The user's ID

        Returns
        -------
        CartData
            The cart data
        """
        cart = Cart(user_id=user_id)
        CartRepository.create(cart)
        return CartData.from_cart(cart, [])

    @staticmethod
    def get_by_user_id(user_id: int) -> CartData:
        """
        Get a cart by user ID

        Parameters
        ----------
        user_id: int
            The user's ID

        Returns
        -------
        CartData
            The cart data
        """
        cart = CartRepository.get_by_user_id(user_id)
        cart_items = CartItemInteractor.get_all_by_cart(cart.id)
        return CartData.from_cart(cart, cart_items)

    @staticmethod
    def clean(user_id: int):
        """
        Clean a cart by removing all cart items

        Parameters
        ----------
        user_id: int
            The user's ID
        """
        CartRepository.clean(user_id)

    @staticmethod
    def add_item(user_id: int, product_id: int, quantity: int):
        """
        Add an item to a cart

        Parameters
        ----------
        user_id: int
            The user's ID
        product_id: int
            The product's ID
        quantity: int
            The quantity
        """
        cart = CartRepository.get_by_user_id(user_id)
        CartItemInteractor.add_item(cart.id, product_id, quantity)

    @staticmethod
    def remove_item(user_id: int, product_id: int):
        """
        Remove an item from a cart

        Parameters
        ----------
        user_id: int
            The user's ID
        product_id: int
            The product's ID
        """
        cart = CartRepository.get_by_user_id(user_id)
        CartItemInteractor.remove_item(cart.id, product_id)

    @staticmethod
    def update_item(user_id: int, product_id: int, quantity: int):
        """
        Update an item in a cart

        Parameters
        ----------
        user_id: int
            The user's ID
        product_id: int
            The product's ID
        quantity: int
            The quantity
        """
        cart = CartRepository.get_by_user_id(user_id)
        CartItemInteractor.update_item(cart.id, product_id, quantity)
