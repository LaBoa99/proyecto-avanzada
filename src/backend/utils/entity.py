from db.sql import Sql


class Entity:
    def __init__(self, instance_name: str, columns: dict):
        self.instance_name = instance_name
        self.columns = columns

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

    def findOne(self, query_config):
        if len(query_config.keys()):
            return Sql.readAll(
                self.instance_name,
                query_config["select"] if "select" in query_config else [],
                options=query_config,
            )
        return Sql.readAll(self.instance_name)

    def create(self, query_config):
        pass

    def update(self, query_config):
        pass

    def destroy(self, id: int):
        pass
