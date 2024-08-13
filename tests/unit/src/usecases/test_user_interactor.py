from src.models import User
from src.usecases.user_interactor import UserInteractor
from unittest.mock import patch
import unittest


class TestUserInteractor(unittest.TestCase):
    @patch("src.usecases.user_interactor.db")
    def test_create(self, db):
        user = User(name="test", email="test@test.com", password="test", type="admin")
        UserInteractor.create(user)
        db.session.add.assert_called_once_with(user)
        db.session.commit.assert_called_once()

    @patch("src.usecases.user_interactor.User")
    def test_get_jwt_token(self, user_mock):
        email = "test@test.com"
        password = "test"
        mock_token = "1234"
        user_mock.create_access_token.return_value = mock_token
        user_mock.query.filter_by.return_value.first.return_value = user_mock

        token = UserInteractor.get_jwt_token(email, password)

        self.assertEqual(mock_token, token)
        user_mock.query.filter_by.assert_called_once_with(email=email)
        user_mock.create_access_token.assert_called_once()
        user_mock.check_password.assert_called_once_with(password)

    @patch("src.usecases.user_interactor.User")
    def test_get_jwt_token_invalid(self, user_mock):
        email = "test@email.com"
        password = "test"
        user_mock.query.filter_by.return_value.first.return_value = None

        token = UserInteractor.get_jwt_token(email, password)

        self.assertIsNone(token)
        user_mock.query.filter_by.assert_called_once_with(email=email)
        user_mock.create_access_token.assert_not_called()
