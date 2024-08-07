from alternativa2 import Alternativa

class Pregunta():
    def __init__(self, enunciado:str, ayuda:str, requerido:bool, lista_alternativa:list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.lista_alternativa = [
            Alternativa(a['contenido'], a['ayuda']) for a in lista_alternativa
        ]
        self.requerido = requerido