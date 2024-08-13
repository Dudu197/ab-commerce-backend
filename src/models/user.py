from flask_bcrypt import Bcrypt
from .shared import db


class User(db.Model):
    bcrypt = Bcrypt()
    __valid_types = ("admin", "customer")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    _type = db.Column(db.String(20), nullable=False)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value not in self.__valid_types:
            raise ValueError(f"Invalid type. Must be one of {self.__valid_types}")
        self._type = value

    @property
    def password(self):
        raise AttributeError("password not readable")

    @password.setter
    def password(self, password: str):
        self.password_hash = self.bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

    def check_password(self, password: str) -> bool:
        """
        Check if the password is correct

        Parameters
        ----------
        password: str
            The password to check

        Returns
        -------
        bool
            True if the password is correct, False otherwise
        """
        return self.bcrypt.check_password_hash(self.password_hash, password)
