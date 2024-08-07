from typing import List
from pregunta3 import Pregunta

class Encuesta():
    def __init__(self, nombre:str, preguntas:list):
        self.nombre = nombre
        self.__preguntas = [
            Pregunta(
                p['enunciado'],
                p['ayuda'],
                p['alternativa'],
                p['requerido']
            ) for p in preguntas
        ]
        self._listados_respuestas = []

    def mostrar_respuestas(self):
        print(self.respuesta)
        for p in self.__preguntas:
            p.mostrar_pregunta()
        
    
    def agregar_listado_respuestas(self, listado_respuestas):
        self._listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list, edad_min:int, edad_max: int):
        super().__init__(nombre, preguntas)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self) -> int:
        return self._edad_min
    
    @edad_min.setter
    def edad_min(self, edad_min) -> None:
        self._edad_min = edad_min

    @property
    def edad_max(self) -> int:
        return self._edad_max
    
    @edad_max.setter
    def edad_max(self, edad_max) -> None:
        self._edad_max = edad_max

    def agregar_listado_respuesta(self, respuestas):
        if self.__edad_min <= respuestas.usuario.edad <= self.__edad_max:
            super().agregar_respuesta(respuestas)


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list, regiones: List[int]):
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    @property
    def regiones(self) -> List[int]:
        return self.__regiones

    @regiones.setter
    def regiones(self, regiones) -> None:
        self.__regiones = regiones

    def agregar_listado_respuestas(self, respuestas):
        if respuestas.usuario.region in self._regiones:
            super().agregar_listado_respuestas(respuestas)