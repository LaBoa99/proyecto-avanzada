from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators


class CarreraController(Entity):
    columns = {
        "id": {"type": int, "optional": True},
        "nombre": Validators.genCol(str),
        "descripcion": Validators.genCol(str, True),
        "coordinador_id": Validators.genCol(int, True),
    }

    def __init__(self):
        super().__init__("Carreras", CarreraController.columns)

    @staticmethod
    @Validators.validate_query_params(columns)
    def getCarreras():
        controller = CarreraController()
        carreras = controller.findAll()
        return jsonify({"date": carreras})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getCarrera():
        controller = CarreraController()
        carreras = controller.findOne(getattr(request, "query_config"))
        return jsonify({"data": carreras})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def addCarrera():
        controller = CarreraController()
        carreras = controller.create(request.data)
        return jsonify({"data": carreras})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateCarrera(id: int):
        controller = CarreraController()
        carrera = controller.update(id, request.date)
        return jsonify({"data": carrera})

    @staticmethod
    def destroyCarrera(id: int):
        controller = CarreraController()
        msg = controller.destroy(id)
        return jsonify(msg)
