from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators


class CentroUniversitarioController(Entity):
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
    def getCentroUniversitarios():
        controller = CentroUniversitarioController()
        centros_universitarios = controller.findAll()
        return jsonify({"date": centros_universitarios})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getCentroUniversitario():
        controller = CentroUniversitarioController()
        centros_universitarios = controller.findOne(getattr(request, "query_config"))
        return jsonify({"data": centros_universitarios})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def addCentroUniversitario():
        controller = CentroUniversitarioController()
        centros_universitarios = controller.create(request.data)
        return jsonify({"data": centros_universitarios})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateCentroUniversitario(id: int):
        controller = CentroUniversitarioController()
        centro_universitario = controller.update(id, request.date)
        return jsonify({"data": centro_universitario})

    @staticmethod
    def destroyCentroUniversitario(id: int):
        controller = CentroUniversitarioController()
        msg = controller.destroy(id)
        return jsonify(msg)
