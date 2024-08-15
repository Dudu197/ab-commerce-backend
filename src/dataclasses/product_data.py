from dataclasses import dataclass
from datetime import datetime
from src.models import Product


@dataclass
class ProductData:
    id: int
    name: str
    price: float
    description: str
    category: str
    image: str
    stock: int
    created_at: datetime
    deleted_at: datetime

    @staticmethod
    def from_product(product: Product) -> "ProductData":
        """
        Create a ProductData object from a Product object

        Parameters
        ----------
        product: Product
            The product object to be converted

        Returns
        -------
        ProductData
            The ProductData object
        """
        return ProductData(
            id=product.id,
            name=product.name,
            price=product.price,
            description=product.description,
            category=product.category,
            image=product.image,
            stock=product.stock,
            created_at=product.created_at,
            deleted_at=product.deleted_at,
        )
