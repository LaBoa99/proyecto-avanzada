from pymysql import Connection, cursors
from db.connection import MariaDB
from functools import wraps


class Sql:
    @staticmethod
    def readAll(instance: str, *columns, **options):
        query = Sql.__prepare_read_query(instance, *columns, **options)
        with Sql.__execute(query=query) as cursor:
            return {f"{instance}": cursor.fetchall()}

    @staticmethod
    def readOne(instance: str, id):
        query = f"SELECT * FROM {instance} WHERE ID = {id}"
        with Sql.__execute(query=query) as cursor:
            return {f"{instance}": cursor.fetchone()}

    @staticmethod
    def destroy(instance: str, id: int):
        query = f"DELETE FROM {instance} WHERE id = '{id}'"
        with Sql.__execute(query=query) as cursor:
            cursor.execute(query)
            return {"msg": f"ENTIDAD {instance} ELIMINADA #{id}"}

    @staticmethod
    def update(instance: str, columns: list[str], update_values, where_values):
        query = f"UPDATE {instance} SET {', '.join([f'{col} = %s' for col in columns])} WHERE {', '.join([f'{col} = %s' for col in where_values.keys()])}"
        print(query)
        with Sql.__get_conexion() as conexion:
            conexion.begin()
            cursor: cursors.Cursor = conexion.cursor()
            with cursor:
                cursor.execute(query, list(update_values) + list(where_values.values()))
                conexion.commit()

    @staticmethod
    def create(instance: str, columns: list[str], insert_values) -> list[int]:
        query = f"INSERT INTO {instance} ({','.join(columns)}) VALUES ({','.join(['%s'] * len(columns))})"
        print(query)
        last_ids = []
        with Sql.__get_conexion() as conexion:
            conexion.begin()
            cursor: cursors.Cursor = conexion.cursor()
            with cursor:
                for values in insert_values:
                    cursor.execute(query, values)
                    last_ids.append(cursor.lastrowid)
                conexion.commit()
        return last_ids

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
    def __get_conexion(conexion=None) -> Connection:
        if conexion != None:
            return conexion
        raise ConnectionError("NO hay conexion a la base de datos")

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
                conexion.commit()
                return cursor
        raise ConnectionError("No hay conexion a base de datos")
