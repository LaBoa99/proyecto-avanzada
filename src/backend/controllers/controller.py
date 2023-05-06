from abc import ABC, abstractmethod


class IController(ABC):
    columns = {}

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def getOne(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def updateWithID(self, id):
        pass

    @abstractmethod
    def destroyWithID(self, id):
        pass
