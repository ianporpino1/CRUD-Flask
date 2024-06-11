from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db
import routes

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)


routes.register_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)