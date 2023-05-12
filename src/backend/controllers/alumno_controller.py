from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators
from utils.routes import Route
from controllers.controller import IController


class AlumnoController(Entity, IController):
    columns = {
        "id": {"type": int, "optional": True},
        "codigo": Validators.genCol(int),
        "nombre": Validators.genCol(str),
        "situacion": Validators.genCol(bool, True),
        "centro_id": Validators.genCol(int),
        "carrera_id": Validators.genCol(int),
    }

    def __init__(self):
        super().__init__("alumnos", AlumnoController.columns)

    @staticmethod
    @Validators.validate_query_params(columns)
    def getAll():
        controller = AlumnoController()
        alumnos = controller.findAll()
        return jsonify({"data": alumnos})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getOne(id):
        print("XD", id)
        controller = AlumnoController()
        alumnos = controller.findOne(id, getattr(request, "query_config"))
        return jsonify({"data": alumnos})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def add():
        controller = AlumnoController()
        alumnos = controller.create(request.get_json())
        return jsonify({"data": alumnos})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateWithID(id: int):
        controller = AlumnoController()
        alumno = controller.update(id, request.get_json())
        return jsonify({"data": alumno})

    @staticmethod
    def destroyWithID(id: int):
        controller = AlumnoController()
        msg = controller.destroy(id)
        return jsonify(msg)


alumno_blueprint = Blueprint("alumnos", __name__)
Route.registerCRUD(alumno_blueprint, AlumnoController, "alumno")
