from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getHelloWorld(self, country: str):
        pass

    @abstractmethod
    def getAll(self, entityName: str):
        pass
