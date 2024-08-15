from src.models import User
from src.repositories.user_repository import UserRepository
from unittest.mock import patch
import unittest


class TestUserRepository(unittest.TestCase):
    @patch("src.repositories.user_repository.db")
    def test_create(self, db):
        user = User(name="test", email="test@test.com", password="test", type="admin")
        UserRepository.create(user)
        db.session.add.assert_called_once_with(user)
        db.session.commit.assert_called_once()

    @patch("src.repositories.user_repository.User")
    def test_get_jwt_token(self, user_mock):
        email = "test@test.com"
        password = "test"
        mock_token = "1234"
        user_mock.create_access_token.return_value = mock_token
        user_mock.query.filter_by.return_value.first.return_value = user_mock

        token = UserRepository.get_jwt_token(email, password)

        self.assertEqual(mock_token, token)
        user_mock.query.filter_by.assert_called_once_with(email=email)
        user_mock.create_access_token.assert_called_once()
        user_mock.check_password.assert_called_once_with(password)

    @patch("src.repositories.user_repository.User")
    def test_get_jwt_token_invalid(self, user_mock):
        email = "test@email.com"
        password = "test"
        user_mock.query.filter_by.return_value.first.return_value = None

        token = UserRepository.get_jwt_token(email, password)

        self.assertIsNone(token)
        user_mock.query.filter_by.assert_called_once_with(email=email)
        user_mock.create_access_token.assert_not_called()
