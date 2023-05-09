from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators
from utils.routes import Route
from controllers.controller import IController


class CentroUniversitarioController(Entity, IController):
    columns = {
        "id": {"type": int, "optional": True},
        "nombre": Validators.genCol(str),
        "ubicacion": Validators.genCol(str, True),
        "descripcion": Validators.genCol(str, True),
        "rector_id": Validators.genCol(int, True),
    }

    def __init__(self):
        super().__init__(
            "centros_universitarios", CentroUniversitarioController.columns
        )

    @staticmethod
    @Validators.validate_query_params(columns)
    def getAll():
        controller = CentroUniversitarioController()
        centros_universitarios = controller.findAll()
        return jsonify({"data": centros_universitarios})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getOne(id):
        controller = CentroUniversitarioController()
        centros_universitarios = controller.findOne(
            id, getattr(request, "query_config")
        )
        return jsonify({"data": centros_universitarios})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def add():
        controller = CentroUniversitarioController()
        centros_universitarios = controller.create(request.data)
        return jsonify({"data": centros_universitarios})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateWithID(id: int):
        controller = CentroUniversitarioController()
        centro_universitario = controller.update(id, request.data)
        return jsonify({"data": centro_universitario})

    @staticmethod
    def destroyWithID(id: int):
        controller = CentroUniversitarioController()
        msg = controller.destroy(id)
        return jsonify(msg)


centro_universitario_blueprint = Blueprint("centro_univeresitarios", __name__)
Route.registerCRUD(
    centro_universitario_blueprint, CentroUniversitarioController, "centroUniversitario"
)
