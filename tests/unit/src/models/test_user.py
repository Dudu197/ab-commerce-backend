from src.models.user import User
import unittest


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
        self.assertEqual(user.type, "admin")

    def test_type_setter_invalid(self):
        user = User()
        with self.assertRaises(ValueError):
            user.type = "invalid"
