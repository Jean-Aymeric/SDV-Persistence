from abc import abstractmethod, ABC

from shared.imodel import IModel


class IView(ABC):
    @property
    @abstractmethod
    def Controller(self):
        pass

    @Controller.setter
    @abstractmethod
    def Controller(self, view):
        pass

    @property
    @abstractmethod
    def Model(self) -> IModel:
        pass

    @Model.setter
    @abstractmethod
    def Model(self, model: IModel):
        pass

    @abstractmethod
    def displayMessage(self, message: str):
        pass

    def displayDatum(self, datum: []):
        pass
