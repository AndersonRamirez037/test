import numpy as np 
from modelos.persona import Persona


class Cliente(Persona):
    def __init__(self, cliente_id, nombre, tel, direccion):
        self.__id = cliente_id
        self.__nombre = nombre
        self.__tel = tel
        self.__direccion = direccion
        self.__historial = np.full((10), fill_value=None)
        self.__numPedidos = 0

    def realizarPedido(self, pedido):
        self.__historia[self.__numPedidos] = pedido
        self.__numPedidos += 1

    def verHistorialPedidos(self):
        for i in range(self.__numPedidos):
            self.__historia[i].mostrar()