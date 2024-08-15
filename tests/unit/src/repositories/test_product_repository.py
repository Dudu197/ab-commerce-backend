from datetime import datetime

from src.models import Product
from src.repositories.product_repository import ProductRepository
from unittest.mock import patch, Mock
import unittest


class TestProductRepository(unittest.TestCase):

    @patch("src.repositories.product_repository.db")
    def test_create_product(self, db):
        product = Product(name="product", price=10)
        ProductRepository.create(product)
        db.session.add.assert_called_once_with(product)
        db.session.commit.assert_called_once()

    @patch("src.repositories.product_repository.Product")
    def test_get_all_products(self, product_mock):
        mock_products = [Mock(), Mock()]
        product_mock.query.filter_by.return_value.all.return_value = mock_products
        products = ProductRepository.get_all()
        self.assertEqual(len(products), 2)
        product_mock.query.filter_by.assert_called_once_with(deleted_at=None)

    @patch("src.repositories.product_repository.Product")
    def test_get_by_id(self, product_mock):
        product_id = 1
        expected_product = Product(name="product", price=10)
        product_mock.query.get.return_value = expected_product
        product = ProductRepository.get_by_id(product_id)
        self.assertEqual(expected_product, product)
        product_mock.query.get.assert_called_once_with(product_id)

    @patch("src.repositories.product_repository.Product")
    def test_get_deleted_by_id(self, product_mock):
        product_id = 1
        returned_product = Product(name="product", price=10, deleted_at=datetime.now())
        expected_product = None
        product_mock.query.get.return_value = returned_product
        product = ProductRepository.get_by_id(product_id)
        self.assertEqual(expected_product, product)
        product_mock.query.get.assert_called_once_with(product_id)

    # @patch("src.repositories.product_repository.db")
    # @patch("src.repositories.product_repository.Product")
    # def test_update_product(self, product_mock):
    #     old_product = Product(
    #         id=1,
    #         name="product",
    #         price=10,
    #         description="description",
    #         category="category",
    #         image="image",
    #         stock=10
    #     )
    #     new_product = Product(
    #         id=1,
    #         name="new product",
    #         price=20,
    #         description="new description",
    #         category="new category",
    #         image="new image",
    #         stock=5
    #     )
    #     product_mock.query.get.return_value = old_product
    #
    #     ProductRepository.update(new_product)
    #     db.session.commit.assert_called_once()
    #     product_mock.query.get.assert_called_once_with(old_product.id)
