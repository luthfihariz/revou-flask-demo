from flask import Flask
from app.auth.apis import auth_blueprint
from app.user.apis import user_blueprint
from infrastructure.db import db, db_init
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(user_blueprint, url_prefix="/user")

# with app.app_context():
#     db_init()