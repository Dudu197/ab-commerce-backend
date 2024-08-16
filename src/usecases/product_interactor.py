from src.repositories import ProductRepository
from src.dataclasses import ProductData
from src.models import Product


class ProductInteractor:
    @classmethod
    def create(
        cls,
        name: str,
        price: float,
        description: str,
        category: str,
        image: str,
        stock: int,
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

        Raises
        -------
        ValueError
            If the product is invalid
        """
        product = Product(
            name=name,
            price=price,
            description=description,
            category=category,
            image=image,
            stock=stock,
        )
        cls.__validate_product_attributes(product)
        ProductRepository.create(product)
        return ProductData.from_product(product)

    @classmethod
    def update(
        cls,
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

        Raises
        -------
        ValueError
            If the product is invalid
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
        cls.__validate_product_attributes(product)
        ProductRepository.update(product)
        return ProductData.from_product(product)

    @classmethod
    def get_all(cls) -> list[ProductData]:
        """
        Get all products

        Returns
        -------
        list[ProductData]
            The list of products
        """
        products = ProductRepository.get_all()
        return [ProductData.from_product(product) for product in products]

    @classmethod
    def get_by_id(cls, product_id: int) -> ProductData:
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
        if product is None:
            return None
        return ProductData.from_product(product)

    @classmethod
    def delete(cls, product_id: int):
        """
        Delete a product

        Parameters
        ----------
        product_id: int
            The product's ID
        """
        ProductRepository.delete(product_id)

    @classmethod
    def __validate_product_attributes(cls, product: Product):
        """
        Validate product attributes

        Parameters
        ----------
        product: Product
            The product to be validated

        Raises
        -------
        ValueError
            If the product is invalid
        """
        if product.name is None:
            raise ValueError("Invalid product name")
        if product.price is None:
            raise ValueError("Invalid product price")
        if product.description is None:
            raise ValueError("Invalid product description")
        if product.category is None:
            raise ValueError("Invalid product category")
        if product.image is None:
            raise ValueError("Invalid product image")
        if product.stock is None:
            raise ValueError("Invalid product stock")
        if product.stock < 0:
            raise ValueError("Invalid product stock")
