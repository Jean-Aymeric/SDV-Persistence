from typing import Any

from model.dbConnector import DBConnector
from shared.data.data import Data
from shared.imodel import IModel


class Model(IModel):
    def __init__(self):
        self.__dbConnector = DBConnector("dbConf.json")

    def getHelloWorld(self, country: str):
        return "It works !"

    def getAll(self, entityName: str):
        jsonData: [dict[str, Any]] = self.__dbConnector.getAllJsonData(entityName)
        data: [Data] = []
        for json in jsonData:
            data.append(Model.__dataConverter(entityName, json))
        return data

    @staticmethod
    def __dataConverter(entityName: str, jsonData: dict[str, Any]) -> Data:
        if entityName == "country":
            from shared.data.country import Country
            return Country.jsonToData(jsonData)
        raise Exception("Unknown entity name")
