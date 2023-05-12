class SiauModel:
    def __init__(self, service) -> None:
        self.service = service
        pass

    def rowToDict(self, data):
        keys = list(self.service.getColumns().keys())
        keys.pop(0)  # se elimina la columna ID
        result = {}
        for i, key in enumerate(keys):
            result[key] = data[i]
        return result
