import numpy as np 

class Reporte():
    def __init__(self, pedidos, nro_pedidos):
        self.__pedidos = pedidos
        self.__nro_pedidos = nro_pedidos
        self.__total_ventas = 0
        self.__costo_total = 0

    @property
    def total_ventas(self):
        return self.__total_ventas
 
    @property
    def costo_total(self):
        return self.__costo_total

    def calcular_totales(self):
        self.__total_ventas = 0
        self.__costo_total  = 0
        for i in range(self.__nro_pedidos):
            self.__total_ventas += self.__pedidos[i].total
            for j in range(self.__pedidos[i].nro_pizzas):
                self.__costo_total += self.__pedidos[i].get_pizza(j).calcular_costo()
 
    def generar_tabla(self):
        self.calcular_totales()
        ganancia = self.__total_ventas - self.__costo_total
 
        arr_nombres  = np.full([50], fill_value=None, dtype=object)
        arr_vendidas = np.full([50], fill_value=0, dtype=int)
        arr_ventas = np.full([50], fill_value=0, dtype=int)
        arr_costos = np.full([50], fill_value=0, dtype=int)
        nro_tipos = 0
 
        for i in range(self.__nro_pedidos):
            for j in range(self.__pedidos[i].nro_pizzas):
                pizza  = self.__pedidos[i].get_pizza(j)
                nombre = pizza.nombre
                costo  = pizza.calcular_costo()
                precio = pizza.precio_venta
 
                encontrado = False
                for k in range(nro_tipos):
                    if arr_nombres[k] == nombre:
                        arr_vendidas[k] = arr_vendidas[k] + 1
                        arr_ventas[k] = arr_ventas[k] + precio
                        arr_costos[k] = arr_costos[k] + costo
                        encontrado = True
                        break
 
                if not encontrado:
                    arr_nombres[nro_tipos] = nombre
                    arr_vendidas[nro_tipos] = 1
                    arr_ventas[nro_tipos] = precio
                    arr_costos[nro_tipos] = costo
                    nro_tipos = nro_tipos + 1
 
        SEP  = "═" * 68
        SEP2 = "─" * 68
        print(f"\n{SEP}")
        print(f"  REPORTE DE VENTAS")
        print(SEP)
        print(f"  Total pedidos : {self.__nro_pedidos}")
        print(f"  Total ventas  : ${self.__total_ventas}")
        print(f"  Costo total   : ${self.__costo_total}")
        print(f"  Ganancia neta : ${ganancia}")
        print(SEP2)
        print(f"  {'Pizza'} {'Vendidas'} {'Ventas'} "
              f"{'Costo'} {'Ganancia'}")
        print(SEP2)
        for k in range(nro_tipos):
            gan   = arr_ventas[k] - arr_costos[k]
            if gan >= 0:
                signo = "✓"
            else:
                signo = "✗"
            print(f"  {signo} {arr_nombres[k]} {arr_vendidas[k]} "
                  f"${arr_ventas[k]} "
                  f"${arr_costos[k]} "
                  f"${gan}")
        print(SEP)