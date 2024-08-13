from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models import User
from src.usecases import UserInteractor
from flask import Blueprint

simple_page = Blueprint("simple_page", __name__, template_folder="templates")


@simple_page.route("/register", methods=["POST"])
def register():
    """
    Register a new user
    ---
    parameters:
      - name: username
        in: body
        type: string
        required: true
        description: The user's username
      - name: password
        in: body
        type: string
        required: true
        description: The user's password
    responses:
      201:
        description: User created successfully
      400:
        description: User already exists
    """
    user = User(
        name=request.json.get("name"),
        email=request.json.get("email"),
        password=request.json.get("password"),
        type=request.json.get("type")
    )

    try:
        UserInteractor.create(user)
    except ValueError:
        return jsonify({"msg": "User already exists"}), 400

    return jsonify({"msg": "User created successfully"}), 201


@simple_page.route("/login", methods=["POST"])
def login():
    """
    Login a user and get a JWT token
    ---
    parameters:
        - name: username
            in: body
            type: string
            required: true
            description: The user's username
        - name: password
            in: body
            type: string
            required: true
            description: The user's password
    responses:
      200:
        description: Successful login
        schema:
            id: access_token
            properties:
                access_token:
                type: string
                description: The JWT token
      401:
        description: Invalid credentials
    """
    jwt_token = UserInteractor.get_jwt_token(
        request.json.get("email"), request.json.get("password")
    )
    if jwt_token is None:
        return jsonify({"msg": "Invalid credentials"}), 401

    return jsonify(access_token=jwt_token), 200


@simple_page.route("/me", methods=["GET"])
@jwt_required()
def protected():
    """
    Access a protected route
    ---
    security:
      - Bearer: []
    responses:
      200:
        description: Successfully accessed protected route
        schema:
          id: user_info
          properties:
            logged_in_as:
              type: string
              description: Username of the logged-in user
    """
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
