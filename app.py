from flask import Flask
from flask_jwt_extended import JWTManager
from src.models import db
from src.routes.user_routes import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super_secret_token'

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
