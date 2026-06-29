import numpy as np 

class Pedido():
    def __init__(self, id_pedido, cliente, tipo):
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__tipo = tipo
        self.__estado = "preparando"
        self.__total = 0
        self.__pizzas = np.full([10], fill_value=None, dtype=object)
        self.__nro_pizzas = 0

    @property
    def id_pedido(self):
        return self.__id_pedido
 
    @property
    def cliente(self):
        return self.__cliente
 
    @property
    def tipo(self):
        return self.__tipo
 
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, e):
        self.__estado = e
 
    @property
    def total(self):
        return self.__total
 
    @property
    def nro_pizzas(self):
        return self.__nro_pizzas

    def agregar_pizza(self, pizza):
        self.__pizzas[self.__nro_pizzas] = pizza
        self.__nro_pizzas += 1

    def calcular_total(self):
        self.__total = 0
        for i in range(self.__nro_pizzas):
            self.__total += self.__pizzas[i].precio_venta
        return self.__total
    
    def get_pizza(self, i):
        return self.__pizzas[i]

    def describir(self): 
        nombres = ""
        for i in range(self.__nro_pizzas):
            nombres += self.__pizzas[i].nombre
            if i < self.__nro_pizzas - 1:
                nombres += ", "
        print(f"  Pedido #{self.__id_pedido} | {self.__cliente.nombre} | "
              f"{self.__tipo} | {self.__estado} | "
              f"Pizzas: {nombres} | Total: ${self.__total}")