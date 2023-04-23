from db.sql import Sql
from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators


# Este controller solo es de prueba
class HelloController(Entity):
    columns = {
        "id": {"type": int, "optional": True},
        "nombre": {
            "type": str,
            "optional": True,
        },
    }

    def __init__(self):
        super().__init__("profesores", HelloController.columns)

    @staticmethod
    @Validators.validate_response(columns)
    @Validators.validate_query_params(columns)
    def hello():
        controller = HelloController()
        profesores = controller.findAll(getattr(request, "query_config"))
        return jsonify({"data": profesores})


# Routes and Register
hello_blueprint = Blueprint("hello", __name__)
hello_blueprint.add_url_rule("/", "hello", HelloController.hello, methods=["POST"])
