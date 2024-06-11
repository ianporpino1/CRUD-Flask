from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from config import Config
from exceptions import *
from models import db
import routes

app = Flask(__name__)

#Error handling metodos
@app.errorhandler(InvalidCredentialsError)
def handle_invalid_credentials_error(error):
    response = jsonify({'error': 'Invalid Credentials', 'message': 'Bad email or password'})
    response.status_code = 400
    return response
@app.errorhandler(UserAlreadyExistsError)
def handle_user_already_exists_error(error):
    response = jsonify({'error': 'User Already Exists', 'message': 'User already exists, try another email'})
    response.status_code = 400
    return response
@app.errorhandler(InvalidInputError)
def handle_invalid_input_error(e):
    response = jsonify({'error': 'Invalid Input', 'message': e.message})
    response.status_code = 400
    return response

#configuracoes do banco(in memory) e jwt
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)


routes.register_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)