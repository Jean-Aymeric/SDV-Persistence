from shared.icontroller import IController
from shared.imodel import IModel
from shared.iview import IView


class Controller(IController):
    __model: IModel = None
    __view: IView = None

    def __init__(self, view, model):
        self.Model = model
        self.View = view

    @property
    def View(self):
        return self.__view

    @property
    def Model(self) -> IModel:
        return self.__model

    @View.setter
    def View(self, view):
        self.__view = view
        if view.Controller != self:
            view.Controller = self
        self.__model = view.Model

    @Model.setter
    def Model(self, model: IModel):
        self.__model = model

    def start(self):
        self.View.displayDatum(self.Model.getAll("country"))
