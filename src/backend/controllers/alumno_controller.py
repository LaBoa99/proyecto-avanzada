from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators


class AlumnoController(Entity):
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
    def getAlumnos():
        controller = AlumnoController()
        alumnos = controller.findAll()
        return jsonify({"date": alumnos})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getAlumno():
        controller = AlumnoController()
        alumnos = controller.findOne(getattr(request, "query_config"))
        return jsonify({"data": alumnos})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def addAlumno():
        controller = AlumnoController()
        alumnos = controller.create(request.data)
        return jsonify({"data": alumnos})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateAlumno(id: int):
        controller = AlumnoController()
        alumno = controller.update(id, request.date)
        return jsonify({"data": alumno})

    @staticmethod
    def destroyAlumno(id: int):
        controller = AlumnoController()
        msg = controller.destroy(id)
        return jsonify(msg)
