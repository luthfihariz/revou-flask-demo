import os
from flask import Flask
from flask import Flask, request
from db import db, db_init
from user.apis import user_blueprint
from auth.apis import auth_blueprint
from common.bcrypt import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)
bcrypt.init_app(app)


app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(auth_blueprint, url_prefix="/auth")

# with app.app_context():
#     db_init()


# def print_registered_routes():
#     routes = []
#     for rule in app.url_map.iter_rules():
#         routes.append((rule.endpoint, rule.methods, str(rule)))
    
#     print("Registered Routes:")
#     for route in routes:
#         print(f"Endpoint: {route[0]}, Methods: {route[1]}, URL: {route[2]}")

# print_registered_routes()