import numpy as np

class Pizza(): 
    def __init__(self, id_pizza, nombre, precio_venta):
        self.__id = id_pizza
        self.__nombre = nombre
        self.__precio_venta = float(precio_venta)
        
        self.__ingredientes = np.full([10], fill_value=None, dtype=object)
        self.__cantidades = np.full([10], fill_value= 0, dtype=float)
        self.__nro_ing = 0

    @property
    def id_pizza(self):
        return self.__id
 
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, n):
        self.__nombre = n
 
    @property
    def precio_venta(self):
        return self.__precio_venta
    @precio_venta.setter
    def precio_venta(self, p):
        self.__precio_venta = float(p)
 
    @property
    def nro_ing(self):
        return self.__nro_ing

    def agregar_ingrediente(self, ingrediente, cantidad):
        self.__ingredientes[self.__nro_ing] = ingrediente
        self.__cantidades[self.__nro_ing]   = cantidad
        self.__nro_ing += 1
 
    def verificar_ingredientes(self):
        for i in range(self.__nro_ing):
            ing  = self.__ingredientes[i]
            cant = self.__cantidades[i]
            if ing.cantidad < cant:
                print(f"Sin ingrediente: '{ing.nombre}' "
                      f"(necesita {cant} {ing.unidad}, hay {ing.cantidad}).")
                return False
        return True
 
    def descontar_ingredientes(self):
        for i in range(self.__nro_ing):
            self.__ingredientes[i].descontar(self.__cantidades[i])
 
    def calcular_costo(self):
        costo = 0.0
        for i in range(self.__nro_ing):
            costo += (self.__ingredientes[i].valor_unitario * self.__cantidades[i])
        return costo
 
    def describir(self):
        print(f"  {self.__nombre} — ${self.__precio_venta}")