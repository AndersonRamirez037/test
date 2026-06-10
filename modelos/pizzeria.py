import numpy as np
from models.pedido import Pedido

class Pizzeria(): 
    def __init__(self, nombre):
        self.__nombre = nombre 
        self.__pedidos = np.full((10), fill_value=None, dtype=Pedido)
        self.__numPedidos = 0


    def registrarPedido(self, pedido):
        self.__pedidos[self.__numPedidos] = pedido
        self.__numPedidos += 1

    def cancelarPedido(self, id):
        for i in range(self.__numPedidos):
            if self.__pedidos[i].__pedidoId == id:
                self.__pedidos[i] = None

    def validarCapacidad(self):
        return self.__numPedidos < 10

    def notificarCliente(self):
        print("Pedido listo!")

    def generarReporte(self):
        total = 0
        for i in range(self.__numPedidos):
            if self.__pedidos[i] is not None: 
                total += self.__pedidos[i].calcularTotal()

        print("Ventas totales: ", total)