from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint

from src.repositories.user_repository import UserRepository
from src.usecases import CartInteractor, OrderInteractor

cart_routes = Blueprint("carts", __name__, template_folder="templates")


@cart_routes.route("/cart", methods=["GET"])
@jwt_required()
def get_cart():
    """
    Get the user's cart
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
    user_email = get_jwt_identity()
    current_user = UserRepository.get_by_email(user_email)
    cart = CartInteractor.get_by_user_id(current_user.id)
    return jsonify(cart), 200


@cart_routes.route("/cart/add", methods=["POST"])
@jwt_required()
def add_item():
    """
    Add an item to the user's cart
    ---
    parameters:
      - name: product_id
        in: body
        type: integer
        required: true
        description: The product id
      - name: quantity
        in: body
        type: integer
        required: true
        description: The quantity
    responses:
      200:
        description: Item added successfully
      400:
        description: Error adding item
    """
    user_email = get_jwt_identity()
    current_user = UserRepository.get_by_email(user_email)
    product_id = request.json.get("product_id")
    quantity = request.json.get("quantity")
    try:
        CartInteractor.add_item(current_user.id, product_id, quantity)
        return jsonify({"msg": "Item added successfully"}), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error adding item"}), 500


@cart_routes.route("/cart/clean", methods=["POST"])
@jwt_required()
def clean_cart():
    """
    Clean the user's cart
    ---
    responses:
      200:
        description: Cart cleaned successfully
      400:
        description: Error cleaning cart
    """
    user_email = get_jwt_identity()
    current_user = UserRepository.get_by_email(user_email)
    CartInteractor.clean(current_user.id)
    return jsonify({"msg": "Cart cleaned successfully"}), 200


@cart_routes.route("/cart/checkout", methods=["POST"])
@jwt_required()
def checkout():
    """
    Checkout the user's cart
    ---
    responses:
      200:
        description: Cart checked out successfully
      400:
        description: Error checking out cart
    """
    user_email = get_jwt_identity()
    current_user = UserRepository.get_by_email(user_email)
    try:
        cart = OrderInteractor.create(current_user.id)
        return jsonify(cart), 200
    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Error checking out cart"}), 500
