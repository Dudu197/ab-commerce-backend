# E-commerce Project

This is a simple e-commerce project that allows users to create products, add products to a cart, and checkout the cart to create an order.

The project is implemented using Python and Flask.

## Project Architecture

This project uses clean architecture to separate the business logic from the infrastructure. The project is divided into the following layers:

- **Usecases**: This layer contains the application business logic. It is divided into usecases, each usecase is a class that contains a single method that represents a business operation. The usecases are independent of the infrastructure and can be easily tested.
- **Models**: This layer contains the domain entities. The entities are plain Python classes that represent the domain objects.
- **Repositories**: This layer contains the interfaces that define the methods that the infrastructure must implement to interact with the database. The repositories are implemented in the infrastructure layer.
- **Dataclasses**: This layer contains the dataclasses that are used to transfer data between the layers of the application.
- **Routes**: This layer contains the Flask routes that define the API endpoints. The routes call the usecases to execute the business logic.

The project also contains a `tests` directory with unit tests for the usecases, models and repositories.

## Database

This project uses an in-memory SQLite database to store the data. The database is created when the application starts and is destroyed when the application stops. The database is created using SQLAlchemy and the data is accessed using the `sqlite3` module.

## Authentication

This project uses JWT tokens for authentication. When a user logs in, a JWT token is generated and returned to the user. The user must include this token in the `Authorization` header of the requests to authenticate.

## Authorization

This project uses role-based authorization to restrict access to certain endpoints. There are two roles: `admin` and `customer`. The `admin` role has access to all endpoints, while the `customer` role has access to a limited set of endpoints.

## Postman Collection

A Postman collection with the API endpoints is available in the `postman` directory.
Be sure to update the authorization token in the collection to match the token generated when you log in.

The collection uses the following variables:

- `ecommerce`: The base URL of the API (e.g. `http://localhost:5000`).

## Setup

### Create a new environment with conda (optional)

```bash
conda create -n ecommerce python=3.10
conda activate ecommerce
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the tests

```bash
python -m unittest discover tests
```

### Run the application

```bash
python app.py
```

## Usage

### Create a new admin user

```bash
curl -X POST http://localhost:5000/register -d '{"name": "alice", "email": "alice@test.com", "password": "1234", "type": "admin"}' -H 'Content-Type: application/json'
```

### Login as an admin user

```bash
curl -X POST http://localhost:5000/login -d '{"email": "alice@test.com", "password": "1234"}' -H 'Content-Type: application/json'
```

This will return a token that you can use to authenticate as a user.

### Create a new product

```bash
curl -X POST http://localhost:5000/products -d '{"name":"Product 1","description":"Product description","price":20,"category":"Cool","stock":10,"image":"http://image.com"}' -H 'Content-Type: application/json' -H "Authorization: Bearer <token>"
```

### Get all products

```bash
curl http://localhost:5000/products
```

### Get a product by ID

```bash
curl http://localhost:5000/products/1
```

### Update a product

```bash
curl -X PUT http://localhost:5000/products/1 -d '{"name":"Product 1","description":"Product description","price":30,"category":"Cool","stock":10,"image":"http://image.com"}' -H 'Content-Type: application/json' -H "Authorization: Bearer <token>"
```

### Delete a product

```bash
curl -X DELETE http://localhost:5000/products/1 -H "Authorization: Bearer <token>"
```

### Create a new user

```bash
curl -X POST http://localhost:5000/register -d '{"name": "bob", "email": "bob@test.com", "password": "1234", "type": "customer"}' -H 'Content-Type: application/json'
```

### Login as a user

```bash
curl -X POST http://localhost:5000/login -d '{"email": "bob@test.com", "password": "1234"}' -H 'Content-Type: application/json'
```

This will return a token that you can use to authenticate as a user.

### Get all products

```bash
curl http://localhost:5000/products
```

### Add a product to the cart

```bash
curl -X POST http://localhost:5000/cart/add -d '{"product_id": 1, "quantity": 2}' -H 'Content-Type: application/json' -H "Authorization: Bearer <token>"
```

### Get the cart

```bash
curl http://localhost:5000/cart -H "Authorization: Bearer <token>"
```

### Checkout the cart (create an order)

```bash
curl -X POST http://localhost:5000/cart/checkout -H "Authorization: Bearer <token>"
```

## Improvements

Due to time constraints, some additional features were not implemented. Here are some improvements that could be made to the project:

- Add Swagger documentation for the API.
- Add Factories for creating test data.
- Add more tests for the routes.