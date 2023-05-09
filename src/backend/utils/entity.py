from utils.validators import Validators
from db.sql import Sql
from typing import Dict, Any


class Entity:
    def __init__(self, instance_name: str, columns: Dict[str, Any]):
        self.instance_name = instance_name
        self.columns = columns
        self.columns_names = list(columns.keys())

    def get_columns(self):
        return self.columns

    def get_instance_name(self):
        return self.instance_name

    def findAll(self, query_config={}):
        if len(query_config.keys()):
            return Sql.readAll(
                self.instance_name,
                query_config["select"] if "select" in query_config else [],
                options=query_config,
            )
        return Sql.readAll(self.instance_name)

    def findOne(self, id, query_config):
        if len(query_config.keys()):
            return Sql.readAll(
                self.instance_name,
                query_config["select"] if "select" in query_config else [],
                options=query_config,
            )
        return Sql.readOne(self.instance_name, id)

    def create(self, data):
        return Sql.create(self.instance_name, self.columns_names, data)

    def update(self, id: int, data):
        if Validators.check_id(id):
            return Sql.update(self.instance_name, self.columns_names, data, {"id": id})

    def destroy(self, id: int):
        if Validators.check_id(id):
            return Sql.destroy(self.instance_name, id)
