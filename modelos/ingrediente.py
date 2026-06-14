class Ingrediente():
    def __init__(self, id_ing, nombre, cantidad, valor_unitario, unidad, stock_minimo): 
        self.__id = id_ing
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__valor_unitario = valor_unitario
        self.__unidad = unidad
        self.__stock_minimo = stock_minimo

    @property
    def id_ing(self):
        return self.__id
 
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, n):
        self.__nombre = n
 
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, c):
        self.__cantidad = c
 
    @property
    def valor_unitario(self):
        return self.__valor_unitario

    @valor_unitario.setter
    def valor_unitario(self, v):
        self.__valor_unitario = v
 
    @property
    def unidad(self):
        return self.__unidad
 
    @property
    def stock_minimo(self):
        return self.__stock_minimo
        
    @stock_minimo.setter
    def stock_minimo(self, s):
        self.__stock_minimo = s

    def hay_stock(self):
        return self.__cantidad > self.__stock_minimo

    def descontar(self, cant): 
        if cant > self.__cantidadDisponible:
            print(f"Sin stock suficiente de {self.__nombre}.")
            return False 
        self.__cantidad -= cant

        if not self.hay_stock():
            print(f"Stock bajo: {self.__nombre} "
                  f"({self.__cantidad} {self.__unidad} restantes).")
        return True    

    def describir(self):
        if self.hay_stock:
            estado = "OK"
        else:
            estado = "BAJO"
        print(f"  [{estado}] {self.__nombre}: "
              f"{self.__cantidad} {self.__unidad} | "
              f"${self.__valor_unitario}/u")