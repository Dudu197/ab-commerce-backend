from dataclasses import dataclass

from src.models import User


@dataclass
class UserData:
    name: str
    email: str
    type: str

    @staticmethod
    def from_user(user: User) -> "UserData":
        """
        Create a UserData object from a User object

        Parameters
        ----------
        user: User
            The user object to be converted

        Returns
        -------
        UserData
            The UserData object
        """
        return UserData(name=user.name, email=user.email, type=user.type.value)
