from main2 import app
from flask import request, current_app
with app.test_request_context('/books'):
    request.path
    request.method
    current_app.name