from shared.icontroller import IController
from shared.imodel import IModel
from shared.iview import IView


class View(IView):
    __controller: IController | None = None
    __model: IModel | None = None

    @property
    def Controller(self):
        return self.__controller

    @property
    def Model(self) -> IModel:
        return self.__model

    @Controller.setter
    def Controller(self, controller):
        self.__controller = controller
        if controller.View != self:
            controller.View = self
        self.__model = controller.Model

    @Model.setter
    def Model(self, model: IModel):
        self.__model = model

    def displayMessage(self, message: str):
        print(message)

    def displayDatum(self, datum: []):
        for data in datum:
            print(data)
