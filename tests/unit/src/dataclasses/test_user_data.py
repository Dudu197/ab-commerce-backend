from src.dataclasses import UserData
from src.models import User
import unittest


class TestUserData(unittest.TestCase):
    def test_from_user(self):
        user = User(id=1, name="user", email="test@test.com", type="customer")
        user_data = UserData.from_user(user)
        self.assertEqual(user_data.name, user.name)
        self.assertEqual(user_data.email, user.email)
        self.assertEqual(user_data.type, user.type.value)
