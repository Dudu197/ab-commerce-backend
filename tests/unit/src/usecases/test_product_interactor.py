from src.dataclasses import ProductData
from src.models import Product
from src.usecases import ProductInteractor
from unittest.mock import patch, Mock
import unittest


class TestProductInteractor(unittest.TestCase):
    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create(self, mock_product_repository):
        product_data = ProductInteractor.create("test", 10.0, "test", "test", "test", 1)
        self.assertEqual(product_data.name, "test")
        self.assertEqual(product_data.price, 10.0)
        mock_product_repository.create.assert_called_once()

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create_invalid_name(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.create(None, 10.0, "test", "test", "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create_invalid_price(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.create("test", None, "test", "test", "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create_invalid_description(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.create("test", 10.0, None, "test", "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create_invalid_category(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.create("test", 10.0, "test", None, "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create_invalid_image(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.create("test", 10.0, "test", "test", None, 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create_invalid_none_stock(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.create("test", 10.0, "test", "test", "test", None)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_create_invalid_negative_stock(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.create("test", 10.0, "test", "test", "test", -1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update(self, mock_product_repository):
        product_data = ProductInteractor.update(
            1, "test", 10.0, "test", "test", "test", 1
        )
        self.assertEqual(product_data.name, "test")
        self.assertEqual(product_data.price, 10.0)
        mock_product_repository.update.assert_called_once()

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update_invalid_name(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.update(1, None, 10.0, "test", "test", "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update_invalid_price(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.update(1, "test", None, "test", "test", "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update_invalid_description(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.update(1, "test", 10.0, None, "test", "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update_invalid_category(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.update(1, "test", 10.0, "test", None, "test", 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update_invalid_image(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.update(1, "test", 10.0, "test", "test", None, 1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update_invalid_none_stock(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.update(1, "test", 10.0, "test", "test", "test", None)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_update_invalid_negative_stock(self, mock_product_repository):
        with self.assertRaises(ValueError):
            ProductInteractor.update(1, "test", 10.0, "test", "test", "test", -1)

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_get_all(self, mock_product_repository):
        mock_product = Mock()
        mock_product.name = "test"
        mock_product.price = 10.0
        mock_product_repository.get_all.return_value = [mock_product]
        products = ProductInteractor.get_all()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "test")
        self.assertEqual(products[0].price, 10.0)
        mock_product_repository.get_all.assert_called_once()

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_get_by_id(self, mock_product_repository):
        product = Product(
            id=1,
            name="test",
            price=10.0,
            description="test",
            category="test",
            image="test",
            stock=1,
        )
        expected_product_data = ProductData(
            id=1,
            name="test",
            price=10.0,
            description="test",
            category="test",
            image="test",
            stock=1,
            created_at=product.created_at,
            deleted_at=product.deleted_at,
        )
        mock_product_repository.get_by_id.return_value = product
        returned_product = ProductInteractor.get_by_id(1)
        self.assertEqual(expected_product_data, returned_product)
        mock_product_repository.get_by_id.assert_called_once()

    @patch("src.usecases.product_interactor.ProductRepository")
    def test_delete(self, mock_product_repository):
        ProductInteractor.delete(1)
        mock_product_repository.delete.assert_called_once_with(1)
