from src.models import User, db


class UserInteractor:
    @staticmethod
    def create(user: User):
        """
        Create a new user

        Parameters
        ----------
        user: User
            The user to be created
        """
        db.session.add(user)
        db.session.commit()

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
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return None

        return user.create_access_token()
