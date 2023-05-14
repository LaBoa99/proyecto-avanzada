from enum import Enum


class MENU_SIAU(Enum):
    ALUMNOS = 1
    PROFESORES = 2
    MATERIAS = 3
    CARRERAS = 4
    CENTROS_UNIVERSITARIOS = 5
    CREDITOS = 6


class INSTANCES_SIAU(Enum):
    ALUMNOS = "alumnos"
    PROFESORES = "profesores"
    MATERIAS = "materias"
    CARRERAS = "carreras"
    CENTROS_UNIVERSITARIOS = "centros_universitarios"
    CREDITOS = ""


class Validators:
    @staticmethod
    def genCol(type, optional=False):
        return {"type": type, "optional": optional}

COL_FK_IDS = {
    "carrera":"carreras",
    "centro":"centros_universitarios",
    "coordinador": "profesores",
    "rector": "profesores",
    "materia": "materias",
}

COL_INSTANCES = {
    INSTANCES_SIAU.ALUMNOS: {
        "id": {"type": int, "optional": True},
        "codigo": Validators.genCol(int),
        "nombre": Validators.genCol(str),
        "situacion": Validators.genCol(bool, True),
        "centro_id": Validators.genCol(int),
        "carrera_id": Validators.genCol(int),
    },
    INSTANCES_SIAU.PROFESORES: {
        "id": {"type": int, "optional": True},
        "nombre": {
            "type": str,
            "optional": False,
        },
    },
    INSTANCES_SIAU.MATERIAS: {
        "id": {"type": int, "optional": True},
        "NRC": Validators.genCol(str),
        "nombre": Validators.genCol(str),
        "creditos": Validators.genCol(int),
        "cupo_disponible": Validators.genCol(int, True),
        "cupo": Validators.genCol(int),
        "carrera_id": Validators.genCol(int),
        "materia_id": Validators.genCol(int),
    },
    INSTANCES_SIAU.CARRERAS: {
        "id": {"type": int, "optional": True},
        "nombre": Validators.genCol(str),
        "descripcion": Validators.genCol(str, True),
        "coordinador_id": Validators.genCol(int, True),
    },
    INSTANCES_SIAU.CENTROS_UNIVERSITARIOS: {
        "id": {"type": int, "optional": True},
        "nombre": Validators.genCol(str),
        "ubicacion": Validators.genCol(str, True),
        "descripcion": Validators.genCol(str, True),
        "rector_id": Validators.genCol(int, True),
    },
}
