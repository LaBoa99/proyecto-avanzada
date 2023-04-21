import pymysql


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
            MariaDB()
        return MariaDB.__instance
    
    def connect(self):
        return pymysql.connect(
            host="localhost",
            user="root",
            password="admin",
            database="siau",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def get_connection(self):
        if self.conn.open:
            return self.conn
        self.conn = self.connect()
        return  self.conn
