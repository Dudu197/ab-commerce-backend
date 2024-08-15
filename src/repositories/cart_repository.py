from src.models import Cart, db
from src.repositories.cart_item_repository import CartItemRepository


class CartRepository:
    @staticmethod
    def create(cart: Cart):
        """
        Create a new cart

        Parameters
        ----------
        cart: Cart
            The cart to be created
        """
        db.session.add(cart)
        db.session.commit()

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
        cart = Cart.query.get(user_id)
        if cart is None:
            cart = Cart(user_id=user_id)
            CartRepository.create(cart)
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
        cart = CartRepository.get_by_user_id(user_id)
        cart_items = CartItemRepository.get_all_by_cart(cart.id)
        for cart_item in cart_items:
            CartItemRepository.delete(cart_item)
