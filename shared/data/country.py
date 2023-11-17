from __future__ import annotations

from typing import Any

from shared.data.data import Data


class Country(Data):
    __code: str
    __name: str
    __idHelloWorld: int

    def __init__(self, idData: int, code: str, name: str, idHelloWorld: int):
        super().__init__(idData)
        self.__code = code
        self.__name = name
        self.__idHelloWorld = idHelloWorld

    @property
    def Code(self) -> str:
        return self.__code

    @Code.setter
    def Code(self, code: str):
        self.__code = code

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, name: str):
        self.__name = name

    @property
    def IdHelloWorld(self) -> int:
        return self.__idHelloWorld

    @IdHelloWorld.setter
    def IdHelloWorld(self, idHelloWorld: int):
        self.__idHelloWorld = idHelloWorld

    def dataToJson(self) -> dict[str, Any]:
        return {"id": self.idData,
                "code": self.__code,
                "name": self.__name,
                "id_helloworld": self.__idHelloWorld}

    @staticmethod
    def jsonToData(jsonData) -> Country:
        return Country(jsonData["id"], jsonData["code"], jsonData["name"], jsonData["id_helloworld"])
