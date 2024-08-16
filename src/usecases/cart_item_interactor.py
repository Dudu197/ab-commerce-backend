from src.models import CartItem
from src.dataclasses import CartItemData
from src.repositories import CartItemRepository
from .product_interactor import ProductInteractor


class CartItemInteractor:
    @classmethod
    def add_item(cls, cart_id: int, product_id: int, quantity: int) -> CartItemData:
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

        Raises
        -------
        ValueError
            If the cart item is invalid
        """
        cart_item = CartItemRepository.get_by_cart_and_product(cart_id, product_id)
        product = ProductInteractor.get_by_id(product_id)
        if cart_item is None:
            cart_item = CartItem(
                cart_id=cart_id, product_id=product_id, quantity=quantity
            )
            cls.__validate_cart_item_attributes(cart_item)
            CartItemRepository.create(cart_item)
        else:
            cart_item.quantity += quantity
            cls.__validate_cart_item_attributes(cart_item)
            CartItemRepository.update(cart_item)
        return CartItemData.from_cart_item(cart_item, product)

    @classmethod
    def remove_item(cls, cart_id: int, product_id: int):
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

    @classmethod
    def update_item(cls, cart_id: int, product_id: int, quantity: int) -> CartItemData:
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

        Raises
        -------
        ValueError
            If the cart item is invalid
        """
        cart_item = CartItemRepository.get_by_cart_and_product(cart_id, product_id)
        if cart_item is not None:
            cart_item.quantity = quantity
            cls.__validate_cart_item_attributes(cart_item)
            CartItemRepository.update(cart_item)
            product = ProductInteractor.get_by_id(product_id)
            return CartItemData.from_cart_item(cart_item, product)
        return None

    @classmethod
    def get_all_by_cart(cls, cart_id: int) -> list[CartItemData]:
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

    @classmethod
    def __validate_cart_item_attributes(cls, cart_item: CartItem):
        """
        Validate cart item attributes

        Parameters
        ----------
        cart_item: CartItem
            The cart item

        Raises
        -------
        ValueError
            If the cart item is invalid
        """
        if cart_item.cart_id is None:
            raise ValueError("Cart ID is required")
        if cart_item.product_id is None:
            raise ValueError("Product ID is required")
        if cart_item.quantity is None:
            raise ValueError("Quantity is required")
        if cart_item.quantity < 1:
            raise ValueError("Quantity must be greater than 0")
        if cart_item.quantity > 100:
            raise ValueError("Quantity must be less than 100")

        product = ProductInteractor.get_by_id(cart_item.product_id)
        if product is None:
            raise ValueError("Product not found")
        if cart_item.quantity > product.stock:
            raise ValueError("Quantity must be less than or equal to product stock")
