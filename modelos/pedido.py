import numpy as np 
class Pedido():
    def __init__(self, id, fecha, estado):
        self.__pedidoId = id
        self.__fecha = fecha
        self.__estado = estado
        self.__total = 0

        self.__pizzas = np.full((10), fill_value=None)
        self.__numPizzas = 0


    def agregarPizza(self, pizza):
        self.__pizzas[self.__numPizzas] = pizza
        self.__numPizzas += 1

    def calcularTotal(self):
        total = 0
        for i in range(self.__numPizzas):
            total += self.__pizzas[i].getPrecio()
        self.__total = total 
        return total 

    def actualizarEstado(self, estado):
        self.__estado = estado 

    def mostrar(self):
        print(f"Pedido: {self.__pedidoId} - Total: {self.__total}")