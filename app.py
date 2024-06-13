from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from config import Config
import exceptions
from models import db
import routes

app = Flask(__name__)



#configuracoes do banco(in memory) e jwt
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)


routes.register_routes(app)
exceptions.register_exceptions(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)