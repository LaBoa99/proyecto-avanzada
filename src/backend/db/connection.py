from functools import wraps

import pymysql
from pymysql import cursors


class MariaDB:
    __instance = None

    def __init__(self):
        if MariaDB.__instance is not None:
            raise Exception(
                "Esta clase es un Singleton. Use el método get_instance() para obtener una instancia."
            )
        self.conn = self.connect()
        MariaDB.__instance = self

    @staticmethod
    def get_instance():
        if MariaDB.__instance is None:
            MariaDB.__instance = MariaDB()
        return MariaDB.__instance

    @staticmethod
    def obtener_conexion():
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                conexion = MariaDB.get_instance().get_connection()
                return f(conexion=conexion, *args, **kwargs)

            return wrapper

        return decorator

    def connect(self):
        return pymysql.connect(
            host="localhost",
            user="root",
            password="admin",
            database="siau",
            cursorclass=cursors.DictCursor,
        )

    def get_connection(self):
        if self.conn.open:
            return self.conn
        self.conn = self.connect()
        return self.conn
