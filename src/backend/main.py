from flask import Flask, jsonify

from controllers.alumno_controller import alumno_blueprint
from controllers.carrera_controller import carrera_blueprint
from controllers.materia_controller import materia_blueprint
from controllers.centro_universitario_controller import centro_universitario_blueprint
from controllers.profesor_controller import profesor_blueprint


app = Flask(__name__)


# Rutas
app.register_blueprint(alumno_blueprint, url_prefix="/alumnos")
app.register_blueprint(profesor_blueprint, url_prefix="/profesores")
app.register_blueprint(carrera_blueprint, url_prefix="/carreras")
app.register_blueprint(materia_blueprint, url_prefix="/materias")
app.register_blueprint(
    centro_universitario_blueprint, url_prefix="/centros_universitarios"
)

if __name__ == "__main__":
    app.run()
