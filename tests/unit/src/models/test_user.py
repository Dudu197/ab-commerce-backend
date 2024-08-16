from src.models.user import User
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
