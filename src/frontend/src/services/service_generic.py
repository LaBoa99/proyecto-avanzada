from utils.vars import BACKEND_URL
from utils.options import COL_INSTANCES, INSTANCES_SIAU, MENU_SIAU
import requests


class Service:
    def __init__(self) -> None:
        self.instance: INSTANCES_SIAU = INSTANCES_SIAU.PROFESORES
        self.url = ""

    def getAll(self):
        print("url", self.url)
        response = requests.get(self.url)
        return self.__getValue(response)

    def create(self, data):
        response = requests.post(self.url, data)
        return self.__getValue(response)

    def update(self, id, data):
        response = requests.put(f"{self.url}{id}", data)
        return self.__getValue(response)

    def getOne(self, id):
        response = requests.get(f"{self.url}{id}")
        return self.__getValue(response)

    def delete(self, id):
        response = requests.delete(f"{self.url}{id}")
        return self.__getValue(response)

    def setInstance(self, instance_value: INSTANCES_SIAU):
        self.instance = instance_value
        self.url = f"{BACKEND_URL}{self.instance.value}/"

    def getColumns(self):
        return COL_INSTANCES[self.instance]

    def __getValue(self, response):
        if response.status_code == 200:
            data = response.json()
            return data
        return None
