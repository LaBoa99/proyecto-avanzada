from flask import Blueprint, jsonify, request
from utils.entity import Entity
from utils.validators import Validators


class MateriaController(Entity):
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
    def getMaterias():
        controller = MateriaController()
        materias = controller.findAll()
        return jsonify({"date": materias})

    @staticmethod
    @Validators.validate_query_params(columns)
    def getMateria():
        controller = MateriaController()
        materias = controller.findOne(getattr(request, "query_config"))
        return jsonify({"data": materias})

    @staticmethod
    @Validators.validate_resquest_body(columns)
    def addMateria():
        controller = MateriaController()
        materias = controller.create(request.data)
        return jsonify({"data": materias})

    @staticmethod
    @Validators.validate_resquest_body(columns, update=True)
    def updateMateria(id: int):
        controller = MateriaController()
        materia = controller.update(id, request.date)
        return jsonify({"data": materia})

    @staticmethod
    def destroyMateria(id: int):
        controller = MateriaController()
        msg = controller.destroy(id)
        return jsonify(msg)
