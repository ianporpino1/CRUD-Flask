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
