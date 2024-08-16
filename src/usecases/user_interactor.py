from src.models import User, db
from src.dataclasses import UserData
from src.repositories import UserRepository


class UserInteractor:
    @classmethod
    def create(cls, name: str, email: str, password: str, user_type: str) -> UserData:
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

        Raises
        -------
        ValueError
            If the user is invalid
        """
        user = User(name=name, email=email, password=password, type=user_type)
        cls.__validate_user_attributes(user)
        cls.__validate_user_password(user)
        cls.__validate_user_unique_email(user)
        UserRepository.create(user)
        return UserData.from_user(user)

    @classmethod
    def update(cls, name: str, email: str, password: str, user_type: str) -> UserData:
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

        Raises
        -------
        ValueError
            If the user is invalid
        """
        user = User(name=name, email=email, password=password, type=user_type)
        cls.__validate_user_attributes(user)
        UserRepository.update(user)
        return UserData.from_user(user)

    @classmethod
    def get_jwt_token(cls, email: str, password: str) -> str:
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

    @classmethod
    def get_by_email(cls, email: str) -> UserData:
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

    @classmethod
    def __validate_user_attributes(cls, user: User):
        """
        Validate a user

        Parameters
        ----------
        user: User
            The user

        Raises
        -------
        ValueError
            If the user is invalid
        """
        if user.name is None or user.name == "":
            raise ValueError("Name is required")
        if user.email is None or user.email == "":
            raise ValueError("Email is required")
        if user.type is None:
            raise ValueError("User type is required")

    @classmethod
    def __validate_user_password(cls, user: User):
        """
        Validate a user password

        Parameters
        ----------
        user: User
            The user

        Raises
        -------
        ValueError
            If the user is invalid
        """
        if not user.has_password():
            raise ValueError("Password is required")

    @classmethod
    def __validate_user_unique_email(cls, user: User):
        """
        Validate a user password

        Parameters
        ----------
        user: User
            The user

        Raises
        -------
        ValueError
            If the user is invalid
        """
        if UserRepository.get_by_email(user.email):
            raise ValueError("Email is already in use")
