import sqlite3

class DB:
    
    __instance = None

    def __init__(self):
        if DB.__instance is not None:
            raise Exception("ERROR")
        self.conn = self.connect()
        DB.__instance = self
        
    @staticmethod
    def get_instace():
        if DB.__instance is None:
            DB.__instance = DB()
        return DB.__instance
        
    def connect(self):
        return sqlite3.connect("prueba.bd")
    
    def get_connection(self):
        return self.connect()
    


def all(tabla, columnas=[]):
    resultados = []
    with DB.get_instace().get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute(f"SELECT  {','.join(columnas) if len(columnas) > 0 else '*'} FROM {tabla}")
        resultados = cursor.fetchall()
        cursor.close()
    return resultados
    
def insert(tabla, columnas, valores=[]):
    query = f"INSERT INTO {tabla} ({','.join(columnas)}) VALUES ({ ','.join(list('?' * len(columnas))) })"
    print(query)
    with DB.get_instace().get_connection() as conexion:
        cursor = conexion.cursor()
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        
class CRUD:
    columnas = []
    columnasInsert = []
    instancia = ""
    
    def getAll(self):
        return all(self.instancia, self.columnas)
    
    def create(self, data):
        return insert(self.instancia, self.columnasInsert, data)
    
    def update(self, id, data):
        pass

    def delete(self, id):
        pass

class Profesores(CRUD):
    def __init__(self) -> None:
        super().__init__()
        self.columnas = ["id", "nombre"]
        self.columnasInsert = ["nombre"]
        self.instancia = "profesores"
        
class Alumnos(CRUD):
    def __init__(self) -> None:
        super().__init__()
        self.columnas = ["id", "nombre", "creditos"]
        self.columnasInsert = ["nombre", "creditos"]
        self.instancia = "alumnos"
        

class TablaView:
    crud : CRUD = None
    
    def changeSelectBox(self, crud):
        self.crud = crud
    
    def presBtnAll(self):
        print(self.crud.getAll())
        
tabla = TablaView()
tabla.changeSelectBox(Profesores())
tabla.changeSelectBox(Alumnos())   
tabla.presBtnAll()
tabla.changeSelectBox(Profesores())
tabla.presBtnAll()


    