from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators


class ProfesorController(Entity):
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
    def getProfesores():
        controller = ProfesorController()
        profesores = controller.findAll()
        return jsonify({"date": profesores})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getProfesor():
        controller = ProfesorController()
        profesores = controller.findOne(getattr(request, "query_config"))
        return jsonify({"data": profesores})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def addProfesor():
        controller = ProfesorController()
        profesores = controller.create(request.data)
        return jsonify({"data": profesores})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateProfesor(id: int):
        controller = ProfesorController()
        profesor = controller.update(id, request.date)
        return jsonify({"data": profesor})

    @staticmethod
    def destroyProfesor(id: int):
        controller = ProfesorController()
        msg = controller.destroy(id)
        return jsonify(msg)
