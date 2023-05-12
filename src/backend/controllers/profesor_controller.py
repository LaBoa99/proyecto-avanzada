from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators
from utils.routes import Route
from controllers.controller import IController


class ProfesorController(Entity, IController):
    columns = {
        "id": {"type": int, "optional": True},
        "nombre": {
            "type": str,
            "optional": False,
        },
    }

    def __init__(self):
        super().__init__("profesores", ProfesorController.columns)

    @staticmethod
    @Validators.validate_query_params(columns)
    def getAll():
        controller = ProfesorController()
        profesores = controller.findAll()
        return jsonify({"data": profesores})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getOne(id):
        controller = ProfesorController()
        profesores = controller.findOne(id, getattr(request, "query_config"))
        return jsonify({"data": profesores})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=False)
    def add():
        controller = ProfesorController()
        profesores = controller.create(request.get_json())
        return jsonify({"data": profesores})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateWithID(id: int):
        controller = ProfesorController()
        profesor = controller.update(id, request.get_json())
        return jsonify({"data": profesor})

    @staticmethod
    def destroyWithID(id: int):
        controller = ProfesorController()
        msg = controller.destroy(id)
        return jsonify(msg)


profesor_blueprint = Blueprint("profesor", __name__)
Route.registerCRUD(profesor_blueprint, ProfesorController, "profesor")
