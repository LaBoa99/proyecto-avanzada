from pymysql import Connection, cursors
from db.connection import MariaDB
from functools import wraps


class Sql:
    @staticmethod
    def readAll(instance, *columns, **options):
        query = Sql.__prepare_read_query(instance, *columns, **options)
        with Sql.__execute(query=query) as cursor:
            return {f"{instance}": cursor.fetchall()}

    @staticmethod
    def readOne(instance, *columns, **options):
        query = Sql.__prepare_read_query(instance, *columns, **options)
        with Sql.__execute(query=query) as cursor:
            return {f"{instance}": cursor.fetchone()}

    # Utils

    @staticmethod
    def __prepare_read_query(instance, *columns, **options):
        cols = "*"
        if not len(columns) == 0:
            cols = ", ".join(columns)

        query = f"SELECT {cols} FROM {instance}"
        return query

    @staticmethod
    @MariaDB.obtener_conexion()
    def __execute(
        query,
        conexion=None,
    ) -> cursors.Cursor:  # type: ignore
        if conexion != None:
            with conexion:
                print(query)
                cursor = conexion.cursor()
                cursor.execute(query)
                return cursor
        raise ConnectionError("No hay conexion a base de datos")
