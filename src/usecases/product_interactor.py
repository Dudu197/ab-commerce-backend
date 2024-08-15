from src.repositories import ProductRepository
from src.dataclasses import ProductData
from src.models import Product


class ProductInteractor:
    @staticmethod
    def create(
        name: str, price: float, description: str, category: str, image: str, stock: int
    ) -> ProductData:
        """
        Create a new product

        Parameters
        ----------
        name: str
            The product's name
        price: float
            The product's price
        description: str
            The product's description
        category: str
            The product's category
        image: str
            The product's image
        stock: int
            The product's stock

        Returns
        -------
        ProductData
            The product data
        """
        product = Product(
            name=name,
            price=price,
            description=description,
            category=category,
            image=image,
            stock=stock,
        )
        ProductRepository.create(product)
        return ProductData.from_product(product)

    @staticmethod
    def update(
        id: int,
        name: str,
        price: float,
        description: str,
        category: str,
        image: str,
        stock: int,
    ) -> ProductData:
        """
        Update a product

        Parameters
        ----------
        id: int
            The product's ID
        name: str
            The product's name
        price: float
            The product's price
        description: str
            The product's description
        category: str
            The product's category
        image: str
            The product's image
        stock: int
            The product's stock

        Returns
        -------
        ProductData
            The product data
        """
        product = Product(
            id=id,
            name=name,
            price=price,
            description=description,
            category=category,
            image=image,
            stock=stock,
        )
        ProductRepository.update(product)
        return ProductData.from_product(product)

    @staticmethod
    def get_all() -> list[ProductData]:
        """
        Get all products

        Returns
        -------
        list[ProductData]
            The list of products
        """
        products = ProductRepository.get_all()
        return [ProductData.from_product(product) for product in products]

    @staticmethod
    def get_by_id(product_id: int) -> ProductData:
        """
        Get a product by ID

        Parameters
        ----------
        product_id: int
            The product's ID

        Returns
        -------
        ProductData
            The product data
        """
        product = ProductRepository.get_by_id(product_id)
        return ProductData.from_product(product)

    @staticmethod
    def delete(product_id: int):
        """
        Delete a product

        Parameters
        ----------
        product_id: int
            The product's ID
        """
        ProductRepository.delete(product_id)
