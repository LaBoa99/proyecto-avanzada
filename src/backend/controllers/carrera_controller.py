from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators
from utils.routes import Route
from controllers.controller import IController


class CarreraController(Entity, IController):
    columns = {
        "id": {"type": int, "optional": True},
        "nombre": Validators.genCol(str),
        "descripcion": Validators.genCol(str, True),
        "coordinador_id": Validators.genCol(int, True),
    }

    def __init__(self):
        super().__init__("carreras", CarreraController.columns)

    @staticmethod
    @Validators.validate_query_params(columns)
    def getAll():
        controller = CarreraController()
        carreras = controller.findAll()
        return jsonify({"data": carreras})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getOne(id):
        controller = CarreraController()
        carreras = controller.findOne(id, getattr(request, "query_config"))
        return jsonify({"data": carreras})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def add():
        controller = CarreraController()
        carreras = controller.create(request.get_json())
        return jsonify({"data": carreras})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateWithID(id: int):
        controller = CarreraController()
        carrera = controller.update(id, request.get_json())
        return jsonify({"data": carrera})

    @staticmethod
    def destroyWithID(id: int):
        controller = CarreraController()
        msg = controller.destroy(id)
        return jsonify(msg)


carrera_blueprint = Blueprint("carreras", __name__)
Route.registerCRUD(carrera_blueprint, CarreraController, "carrera")
