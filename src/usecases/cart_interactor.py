from src.models import Cart, CartItem, Product, db
from src.repositories import CartRepository
from src.usecases import CartItemInteractor


class CartInteractor:
    @staticmethod
    def create(user_id: int):
        """
        Create a new cart

        Parameters
        ----------
        user_id: int
            The user's ID
        """
        cart = Cart(user_id=user_id)
        CartRepository.create(cart)

    @staticmethod
    def get_by_user_id(user_id: int) -> Cart:
        """
        Get a cart by user ID

        Parameters
        ----------
        user_id: int
            The user's ID

        Returns
        -------
        Cart
            The cart
        """
        cart = CartRepository.get_by_user_id(user_id)
        return cart

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
