from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators
from utils.routes import Route
from controllers.controller import IController


class MateriaController(Entity, IController):
    columns = {
        "id": {"type": int, "optional": True},
        "NRC": Validators.genCol(str),
        "nombre": Validators.genCol(str),
        "creditos": Validators.genCol(int),
        "cupo_disponible": Validators.genCol(int, True),
        "cupo": Validators.genCol(int),
        "carrera_id": Validators.genCol(int),
        "materia_id": Validators.genCol(int),
    }

    def __init__(self):
        super().__init__("materias", MateriaController.columns)

    @staticmethod
    @Validators.validate_query_params(columns)
    def getAll():
        controller = MateriaController()
        materias = controller.findAll()
        return jsonify({"date": materias})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getOne():
        controller = MateriaController()
        materias = controller.findOne(getattr(request, "query_config"))
        return jsonify({"data": materias})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def add():
        controller = MateriaController()
        materias = controller.create(request.data)
        return jsonify({"data": materias})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateWithID(id: int):
        controller = MateriaController()
        materia = controller.update(id, request.date)
        return jsonify({"data": materia})

    @staticmethod
    def destroyWithID(id: int):
        controller = MateriaController()
        msg = controller.destroy(id)
        return jsonify(msg)


materia_blueprint = Blueprint("materias", __name__)
Route.registerCRUD(materia_blueprint, MateriaController, "materia")
