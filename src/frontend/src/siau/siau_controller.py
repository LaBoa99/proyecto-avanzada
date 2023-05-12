from utils.options import COL_INSTANCES, INSTANCES_SIAU


class SiauController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.connect_signals()
        self.change_table(INSTANCES_SIAU.PROFESORES)

    def connect_signals(self):
        self.view.onOptionEvent.connect(self.change_table)
        self.view.onCreateItemEvent.connect(self.create)
        self.view.onUpdateItemEvent.connect(self.update)
        self.view.onDeleteItemEvent.connect(self.delete)

    def create(self, data):
        result = self.model.rowToDict(data)
        self.model.service.create(result)
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass

    def change_table(self, option: INSTANCES_SIAU):
        if option == INSTANCES_SIAU.CREDITOS:
            pass
        else:
            self.model.service.setInstance(option)
            self.view.setColumns(self.model.service.getColumns())
            data = self.model.service.getAll()
            if "data" in data:
                if self.model.service.instance.value in data["data"]:
                    data = data["data"][self.model.service.instance.value]
                    self.view.setRows(self.model.service.getColumns(), data)
            elif "msg" in data:
                print(data["msg"])
            else:
                print("Incorrect Response")