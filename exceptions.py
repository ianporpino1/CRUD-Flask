from flask import Flask, jsonify

class InvalidCredentialsError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class InvalidInputError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(message)


def register_exceptions(app):
    #Error handling metodos
    @app.errorhandler(InvalidCredentialsError)
    def handle_invalid_credentials_error(error):
        response = jsonify({'error': 'Invalid Credentials', 'message': 'Bad email or password'}, 401)
        response.status_code
        return response
    @app.errorhandler(UserAlreadyExistsError)
    def handle_user_already_exists_error(error):
        response = jsonify({'error': 'User Already Exists', 'message': 'User already exists, try another email'},400)
        response.status_code = 400
        return response
    @app.errorhandler(InvalidInputError)
    def handle_invalid_input_error(error):
        response = jsonify({'error': 'Invalid Input', 'message': error.message},error.code)
        response.status_code = error.code
        return response