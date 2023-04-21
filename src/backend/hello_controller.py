from flask import Blueprint, jsonify
from db.connection import MariaDB
hello_blueprint = Blueprint("hello", __name__)


@hello_blueprint.route("/")
def hello():
    connection = MariaDB.get_instance().get_connection()
    profesores = []
    with connection:
        with connection.cursor() as cursor: 
            sql = "SELECT * FROM profesores;"
            cursor.execute(sql)
            profesores = cursor.fetchall()
    return jsonify({"message": "Hola, mundo!", "profesores": profesores})