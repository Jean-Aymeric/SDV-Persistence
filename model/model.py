from shared.imodel import IModel


class Model(IModel):
    def getHelloWorld(self, country: str):
        return "It works !"
