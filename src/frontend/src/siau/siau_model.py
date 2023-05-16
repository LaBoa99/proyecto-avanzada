from utils.options import COL_FK_IDS, COL_FK_INSTANCES, COL_INSTANCES


class SiauModel:
    def __init__(self, service) -> None:
        self.service = service

    def rowToDict(self, data):
        keys = list(self.service.getColumns().keys())
        keys.pop(0)  # se elimina la columna ID
        result = {}
        for i, key in enumerate(keys):
            result[key] = data[i]
        return result
    
    def getExtras(self):
        extras = {}
        for key, value in self.service.getColumns().items():
            if value["type"] == list:
                extras[key] = self.getInstances(key.split("_")[0])
        return extras
    
    def getInstances(self, entity_name):
        data = self.service.getAllGeneric(COL_FK_IDS[entity_name])
        # return list(map(lambda d: d['id'], data)) if data != None else []
        return self.formatData(data, entity_name) if data != None else []
    
    def formatData(self, response, entity_name):
        data = self.__unwrap(response)
        cols = list(COL_INSTANCES[COL_FK_INSTANCES[entity_name]].keys())
        data_sorted = []
        for row in data:
            row_sorted = {}
            for col in cols:
                if col in row:
                    row_sorted[col] = row[col]
            data_sorted.append(row_sorted)
        return data_sorted
    
        
    def __unwrap(self, response):
        return list(response["data"].values())[0]
