from src.models import User
from src.dataclasses import UserData
from src.usecases import UserInteractor
from unittest.mock import patch, Mock
import unittest


class TestUserInteractor(unittest.TestCase):
    @patch("src.usecases.user_interactor.UserRepository")
    def test_create(self, mock_user_repository):
        user_data = UserInteractor.create("test", "test@test.com", "password", "admin")
        self.assertEqual(user_data.name, "test")
        self.assertEqual(user_data.email, "test@test.com")
        self.assertEqual(user_data.type, "admin")
        mock_user_repository.create.assert_called_once()

    @patch("src.usecases.user_interactor.UserRepository")
    def test_update(self, mock_user_repository):
        user_data = UserInteractor.update("test", "test@test.com", "password", "admin")
        self.assertEqual(user_data.name, "test")
        self.assertEqual(user_data.email, "test@test.com")
        self.assertEqual(user_data.type, "admin")
        mock_user_repository.update.assert_called_once()

    @patch("src.usecases.user_interactor.UserRepository")
    def test_get_jwt_token(self, mock_user_repository):
        mock_user = Mock()
        mock_user.create_access_token.return_value = "token"
        mock_user_repository.get_by_email.return_value = mock_user
        token = UserInteractor.get_jwt_token("test@test.com", "password")
        self.assertEqual(token, "token")
        mock_user.create_access_token.assert_called_once()

    @patch("src.usecases.user_interactor.UserRepository")
    def test_get_by_email(self, mock_user_repository):
        user = User(
            name="test", email="test@test.com", password="password", type="admin"
        )
        expected_user_data = UserData(name="test", email="test@test.com", type="admin")
        mock_user_repository.get_by_email.return_value = user
        returned_user = UserInteractor.get_by_email("test@test.com")
        self.assertEqual(expected_user_data, returned_user)
        mock_user_repository.get_by_email.assert_called_once()
