from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint

from src.models import Product
from src.repositories.user_repository import UserRepository
from src.repositories.product_repository import ProductRepository

product_routes = Blueprint("products", __name__, template_folder="templates")


def auth_admin_user(func):
    """
    Decorator to check if the user is an admin
    """

    def wrapper_func():
        user_email = get_jwt_identity()
        current_user = UserRepository.get_by_email(user_email)
        if not current_user.is_admin():
            return jsonify({"msg": "Unauthorized"}), 401
        func()

    return wrapper_func


@product_routes.route("/products", methods=["GET"])
def list_products():
    """
    Get all products
    ---
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
    products = ProductRepository.get_all()
    return jsonify([{"name": product.name} for product in products]), 200


@product_routes.route("/products/<int:id>", methods=["GET"])
def get_product(id: int):
    """
    Get a product by id
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: The product id
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
    product = ProductRepository.get_by_id(id)
    return jsonify(product), 200


@product_routes.route("/products", methods=["POST"])
@jwt_required()
@auth_admin_user
def add():
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
    product = Product(
        name=request.json.get("name"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        category=request.json.get("category"),
        image=request.json.get("image"),
        stock=request.json.get("stock"),
    )
    ProductRepository.create(product)
    return jsonify(product), 200


@product_routes.route("/products/<int:id>", methods=["PUT"])
@jwt_required()
def update(id: int):
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
    product = Product(
        id=id,
        name=request.json.get("name"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        category=request.json.get("category"),
        image=request.json.get("image"),
        stock=request.json.get("stock"),
    )
    ProductRepository.update(product)
    return jsonify(product), 200


@product_routes.route("/products/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id: int):
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
    ProductRepository.delete(id)
    return jsonify({"msg": "Product deleted"}), 200
