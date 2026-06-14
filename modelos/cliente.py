import numpy as np 
from modelos.persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, telefono, direccion):
        super().__init__(nombre, telefono)
        self.__direccion = direccion

    @property 
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, d):
        self.__direccion = d