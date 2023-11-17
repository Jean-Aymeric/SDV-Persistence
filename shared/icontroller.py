from abc import ABC, abstractmethod

from shared.imodel import IModel


class IController(ABC):
    @property
    @abstractmethod
    def View(self):
        pass

    @View.setter
    @abstractmethod
    def View(self, view):
        pass

    @property
    @abstractmethod
    def Model(self) -> IModel:
        pass

    @Model.setter
    @abstractmethod
    def Model(self, model: IModel):
        pass
