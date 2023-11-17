from model.dbConnector import DBConnector
from shared.imodel import IModel


class Model(IModel):
    def __init__(self):
        self.__dbConnector = DBConnector("dbConf.json")
        
    def getHelloWorld(self, country: str):
        return "It works !"
