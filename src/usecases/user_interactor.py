from src.models import User, db
from src.dataclasses import UserData
from src.repositories import UserRepository


class UserInteractor:
    @staticmethod
    def create(name: str, email: str, password: str, user_type: str) -> UserData:
        """
        Create a new user

        Parameters
        ----------
        name: str
            The user's name
        email: str
            The user's email
        password: str
            The user's password
        user_type: str
            The user's type

        Returns
        -------
        UserData
            The user data
        """
        user = User(name=name, email=email, password=password, type=user_type)
        UserRepository.create(user)
        return UserData.from_user(user)

    @staticmethod
    def update(name: str, email: str, password: str, user_type: str) -> UserData:
        """
        Update a user

        Parameters
        ----------
        name: str
            The user's name
        email: str
            The user's email
        password: str
            The user's password
        user_type: str
            The user's type

        Returns
        -------
        UserData
            The user data
        """
        user = User(name=name, email=email, password=password, type=user_type)
        UserRepository.update(user)
        return UserData.from_user(user)

    @staticmethod
    def get_jwt_token(email: str, password: str) -> str:
        """
        Get a JWT token for a user

        Parameters
        ----------
        email: str
            The user's email
        password: str
            The user's password

        Returns
        -------
        str
            The JWT token
        """
        user = UserRepository.get_by_email(email)
        if not user or not user.check_password(password):
            return None

        return user.create_access_token()

    @staticmethod
    def get_by_email(email: str) -> UserData:
        """
        Get a user by email

        Parameters
        ----------
        email: str
            The user's email

        Returns
        -------
        UserData
            The user data
        """
        user = UserRepository.get_by_email(email)
        return UserData.from_user(user)
