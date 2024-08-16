from src.models import CartItem, db


class CartItemRepository:
    @staticmethod
    def create(cart_item: CartItem):
        """
        Create a new cart item

        Parameters
        ----------
        cart_item: CartItem
            The cart item to be created
        """
        db.session.add(cart_item)
        db.session.commit()

    @staticmethod
    def get_all_by_cart(cart_id: int) -> list[CartItem]:
        """
        Get all cart items

        Parameters
        ----------
        cart_id: int
            The cart's ID

        Returns
        -------
        list[CartItem]
            The list of cart items
        """
        return CartItem.query.filter_by(cart_id=cart_id).all()

    @staticmethod
    def get_by_id(cart_item_id: int) -> CartItem:
        """
        Get a cart item by ID

        Parameters
        ----------
        cart_item_id: int
            The cart item's ID

        Returns
        -------
        CartItem
            The cart item
        """
        return CartItem.query.get(cart_item_id)

    @staticmethod
    def get_by_cart_and_product(cart_id: int, product_id: int) -> CartItem:
        """
        Get a cart item by cart and product

        Parameters
        ----------
        cart_id: int
            The cart's ID
        product_id: int
            The product's ID

        Returns
        -------
        CartItem
            The cart item
        """
        return CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()

    @staticmethod
    def update(cart_item: CartItem):
        """
        Update a cart item

        Parameters
        ----------
        cart_item: CartItem
            The cart item to be updated
        """
        db.session.commit()

    @staticmethod
    def delete(cart_item: CartItem):
        """
        Remove a cart item

        Parameters
        ----------
        cart_item: CartItem
            The cart item to be removed
        """
        db.session.delete(cart_item)
        db.session.commit()
