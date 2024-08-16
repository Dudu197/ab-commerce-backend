from src.models.user import User
from unittest.mock import patch
import unittest

from src.models.user_type import UserType


class TestUserModel(unittest.TestCase):
    def test_password_setter(self):
        user = User()
        user.password = "test"
        self.assertTrue(user.password_hash is not None)

    def test_check_password(self):
        user = User()
        password = "test"
        user.password = password
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.check_password("test2"))

    def test_type_setter(self):
        user = User()
        user.type = "admin"
        self.assertEqual(user.type, UserType.ADMIN)

    def test_type_setter_invalid(self):
        user = User()
        with self.assertRaises(ValueError):
            user.type = "invalid"

    @patch("src.models.user.create_access_token")
    def test_create_access_token(self, mock_create_access_token):
        mock_create_access_token.return_value = "test"
        user = User()
        user.email = "test@test.com"
        token = user.create_access_token()
        self.assertEqual(token, "test")

    def test_is_admin(self):
        user = User()
        user.type = UserType.ADMIN
        self.assertTrue(user.is_admin())

    def test_is_not_admin(self):
        user = User()
        user.type = UserType.CUSTOMER
        self.assertFalse(user.is_admin())

    def test_has_password(self):
        user = User()
        user.password = "test"
        self.assertTrue(user.has_password())
