from src.dataclasses import ProductData
from src.models import Product
import unittest


class TestProductData(unittest.TestCase):
    def test_from_product(self):
        product = Product(
            id=1,
            name="product",
            price=10.0,
            description="description",
            category="category",
            image="image",
            stock=10,
        )
        product_data = ProductData.from_product(product)
        self.assertEqual(product_data.id, product.id)
        self.assertEqual(product_data.name, product.name)
        self.assertEqual(product_data.price, product.price)
        self.assertEqual(product_data.description, product.description)
        self.assertEqual(product_data.category, product.category)
        self.assertEqual(product_data.image, product.image)
        self.assertEqual(product_data.stock, product.stock)
