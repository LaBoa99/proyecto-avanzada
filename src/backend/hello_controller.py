from flask import Blueprint, jsonify

hello = Blueprint("hello_controller", __name__)


@hello.route("/hello")
def hello():
    return jsonify({"message": "Hola, mundo!"})
