from usuario5 import Usuario
from typing import List

class ListadoRespuestas():
    def __init__(self, usuario: Usuario, respuestas: list) -> None:
        self._usuario = Usuario
        self._respuestas = respuestas
    
    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @property
    def respuestas(self) -> List[Respuesta]:
        return self._respuestas

