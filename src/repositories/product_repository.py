from datetime import datetime
from src.models import Product, db


class ProductRepository:
    @staticmethod
    def create(product: Product):
        """
        Create a new product

        Parameters
        ----------
        product: Product
            The product to be created
        """
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def get_all() -> list[Product]:
        """
        Get all products

        Returns
        -------
        list[Product]
            The list of products
        """
        return Product.query.filter_by(deleted_at=None).all()

    @staticmethod
    def get_by_id(product_id: int) -> Product:
        """
        Get a product by ID

        Parameters
        ----------
        product_id: int
            The product's ID

        Returns
        -------
        Product
            The product
        """
        product = Product.query.get(product_id)
        if product.deleted_at is not None:
            return None
        return product

    @staticmethod
    def update(product: Product):
        """
        Update a product

        Parameters
        ----------
        product: Product
            The product to be updated
        """
        old_product = ProductRepository.get_by_id(product.id)
        old_product.name = product.name
        old_product.description = product.description
        old_product.price = product.price
        old_product.category = product.category
        old_product.image = product.image
        old_product.stock = product.stock
        db.session.commit()

    @staticmethod
    def delete(product_id: int):
        """
        Delete a product

        Parameters
        ----------
        product_id: int
            The product's ID
        """
        product = ProductRepository.get_by_id(product_id)
        product.deleted_at = datetime.now()
        db.session.commit()
