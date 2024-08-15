from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models import User
from src.usecases import UserInteractor
from flask import Blueprint

user_routes = Blueprint("simple_page", __name__, template_folder="templates")


@user_routes.route("/register", methods=["POST"])
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
    try:
        return (
            jsonify(
                UserInteractor.create(
                    name=request.json.get("name"),
                    email=request.json.get("email"),
                    password=request.json.get("password"),
                    user_type=request.json.get("type"),
                )
            ),
            201,
        )
    except ValueError:
        return jsonify({"msg": "User already exists"}), 400


@user_routes.route("/login", methods=["POST"])
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


@user_routes.route("/users", methods=["PUT"])
@jwt_required()
def update_user():
    """
    Update a user
    ---
    security:
      - Bearer: []
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
            description: User updated successfully
        400:
            description: User not found
    """
    try:
        return (
            jsonify(
                UserInteractor.update(
                    name=request.json.get("name"),
                    email=request.json.get("email"),
                    password=request.json.get("password"),
                    user_type=request.json.get("type"),
                )
            ),
            200,
        )
    except ValueError as e:
        return jsonify({"msg": f"Error updating user: {e}"}), 400


@user_routes.route("/me", methods=["GET"])
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
    email = get_jwt_identity()
    user = UserInteractor.get_by_email(email)
    return jsonify(user), 200
