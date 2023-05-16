from utils.options import INSTANCES_SIAU


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
        self.refresh()

    def update(self, id, data):
        result = self.model.rowToDict(data)
        self.model.service.update(id, result)
        self.refresh()

    def delete(self, id):
        self.model.service.delete(id)
        self.refresh()

    def change_table(self, option: INSTANCES_SIAU):
        if option == INSTANCES_SIAU.CREDITOS:
            self.view.showCredits()
        else:
            self.model.service.setInstance(option)
            self.view.setExtras(self.model.getExtras())
            self.view.setColumns(self.model.service.getColumns())
            data = self.model.service.getAll()
            if "data" in data:
                if self.model.service.instance.value in data["data"]:
                    data = self.model.formatData(data, self.model.service.instance.value)
                    self.view.setRows(self.model.service.getColumns(), data)
                    self.view.setHeader(self.model.service.instance.value)
            elif "msg" in data:
                print(data["msg"])
            else:
                print("Incorrect Response")
                
    def refresh(self):
        self.change_table(self.model.service.instance)
