import pymysql


class MariaDB:
    __instance = None

    def __init__(self):
        if MariaDB.__instance is not None:
            raise Exception(
                "Esta clase es un Singleton. Use el método get_instance() para obtener una instancia."
            )
        self.conn = pymysql.connect(
            host="localhost",
            user="usuario",
            password="contraseña",
            database="nombre_base_de_datos",
            cursorclass=pymysql.cursors.DictCursor,
        )
        MariaDB.__instance = self

    @staticmethod
    def get_instance():
        if MariaDB.__instance is None:
            MariaDB()
        return MariaDB.__instance

    def get_connection(self):
        return self.conn
