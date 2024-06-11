from flask import Flask, jsonify

class InvalidCredentialsError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
