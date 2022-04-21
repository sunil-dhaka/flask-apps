from hashlib import new
from flask import Flask

new_app=Flask(__name__)

@new_app.route("/")
def hello():
    return "<p>Hello, World!</p>"
