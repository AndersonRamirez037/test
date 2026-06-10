class Ingrediente():
    def __init__(self, id, nombre, cantidad, valor): 
        self.__id = id
        self.__nombre = nombre
        self.__cantidadDisponible = cantidad
        self.__valorUnitario = valor

    def hayStock(self, cantidad):
        return self.__cantidadDisponible >= cantidad

    def descontarCantidad(self, cantidad):
        if self.hayStock(cantidad):
            self.__cantidadDisponible -= 1        