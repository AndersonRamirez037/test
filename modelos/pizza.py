import numpy as np

class Pizza(): 
    def __init__(self, id, nombre, descripcion, tamano, precio):
        self.__pizzaId = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__tamano = tamano
        self.__precio = precio
        self.__disponible = True

        self.__ingredientes = np.full([10], fill_value=None)
        self.__cantIng = 0

    def agregarIngrediente(self, ingrediente):
        self.__ingredientes[self.__cantIng] = ingrediente
        self.__cantIng += 1

    def verificarIngrediente(self, ingrediente): 
        for i in range(self.__cantIng):
            if self.__ingredientes[i].hayStock == False:
                return False 
        
        return True 

    def descontarIngrediente(self, ingrediente):
        for i in range(self.__cantIng):
            self.__ingredientes[i].descontarCantidad(1)


    def getPrecio(self):
        return self.__precio

    def getNombre(self):
        return self.__nombre