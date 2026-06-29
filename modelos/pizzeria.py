import numpy as np
from modelos.ingrediente import Ingrediente
from modelos.pizza import Pizza
from modelos.pedido import Pedido
from modelos.reporte import Reporte
 
 
class Pizzeria:
 
    def __init__(self, nombre, departamento, capacidad_maxima):
        self.__nombre = nombre
        self.__departamento = departamento
        self.__capacidad_maxima = capacidad_maxima
        self.__pizzas_en_prod = 0
 
        self.__inventario = np.full([20], fill_value=None, dtype=object)
        self.__catalogo = np.full([10], fill_value=None, dtype=object)
        self.__pedidos = np.full([50], fill_value=None, dtype=object)
        self.__nro_ing = 0
        self.__nro_pizzas = 0
        self.__nro_pedidos = 0
 
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, n):
        self.__nombre = n
 
    @property
    def departamento(self):
        return self.__departamento
 
    @property
    def capacidad_maxima(self):
        return self.__capacidad_maxima

    @capacidad_maxima.setter
    def capacidad_maxima(self, c):
        self.__capacidad_maxima = int(c)
 
    @property
    def pizzas_en_prod(self):
        return self.__pizzas_en_prod
 
    @property
    def nro_pedidos(self):
        return self.__nro_pedidos
 
    def cargar_ingredientes(self):
        fichero = open("datos/ingredientes.csv", "r")
        lineas  = fichero.readlines()
        for linea in lineas: 
            datos = linea.strip().split(";")
            self.__inventario[self.__nro_ing] = Ingrediente(
                datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]
            )
            self.__nro_ing = self.__nro_ing + 1
        fichero.close()
        print(f" {self.__nro_ing} ingredientes cargados.")
 
    def cargar_pizzas(self):
        fichero = open("datos/pizzas.csv", "r")
        lineas  = fichero.readlines()
        for linea in lineas:
            datos = linea.strip().split(";")
            pizza = Pizza(datos[0], datos[1], datos[2])
            ids = datos[3].split("-")
            cants = datos[4].split("-")
            for k in range(len(ids)):
                ing = self._buscar_ingrediente(int(ids[k]))
                if ing is not None:
                    pizza.agregar_ingrediente(ing, float(cants[k]))
            self.__catalogo[self.__nro_pizzas] = pizza
            self.__nro_pizzas += 1
        fichero.close()
        print(f"{self.__nro_pizzas} pizzas cargadas.")
 
    def validar_capacidad(self):
        return self.__pizzas_en_prod < self.__capacidad_maxima
 
    def registrar_pedido(self, cliente, pizzas_sel, nro_sel, tipo):
        if not self.validar_capacidad():
            print(f"\nCocina llena ({self.__capacidad_maxima} pizzas máximo).")
            return None
 
        for i in range(nro_sel):
            if not pizzas_sel[i].verificar_ingredientes():
                print(f"\nNo se puede preparar '{pizzas_sel[i].nombre}'.")
                return None
 
        for i in range(nro_sel):
            pizzas_sel[i].descontar_ingredientes()
 
        pedido = Pedido(self.__nro_pedidos + 1, cliente, tipo)
        for i in range(nro_sel):
            pedido.agregar_pizza(pizzas_sel[i])
        pedido.calcular_total()
 
        self.__pedidos[self.__nro_pedidos] = pedido
        self.__nro_pedidos = self.__nro_pedidos + 1
        self.__pizzas_en_prod = self.__pizzas_en_prod + nro_sel
 
        fichero = open("datos/pedidos.csv", "a")
        nombres_pizzas = ""
        for i in range(pedido.nro_pizzas):
            nombres_pizzas = nombres_pizzas + pedido.get_pizza(i).nombre
            if i < pedido.nro_pizzas - 1:
                nombres_pizzas = nombres_pizzas + "|"
        fichero.writelines([
            f"{pedido.id_pedido};{cliente.nombre};{cliente.telefono};"
            f"{tipo};{pedido.estado};{nombres_pizzas};{pedido.total}\n"
        ])
        fichero.close()
 
        print(f"\n  Pedido #{pedido.id_pedido} registrado — "
              f"{cliente.nombre} | ${pedido.total}")
        return pedido
 
    def cancelar_pedido(self, id_pedido):
        for i in range(self.__nro_pedidos):
            if self.__pedidos[i].id_pedido == id_pedido:
                if self.__pedidos[i].estado != "preparando":
                    print(f"  El pedido #{id_pedido} ya está "
                          f"'{self.__pedidos[i].estado}' y no puede cancelarse.")
                    return
                self.__pizzas_en_prod = self.__pizzas_en_prod - self.__pedidos[i].nro_pizzas
                for j in range(i, self.__nro_pedidos - 1):
                    self.__pedidos[j] = self.__pedidos[j + 1]
                self.__pedidos[self.__nro_pedidos - 1] = None
                self.__nro_pedidos = self.__nro_pedidos - 1
                print(f"  Pedido #{id_pedido} cancelado.")
                return
        print(f"  Pedido #{id_pedido} no encontrado.")

    def _eliminar_pedido_csv(self, id_pedido):
        fichero  = open("datos/pedidos.csv", "r")
        lineas   = fichero.readlines()
        fichero.close()
 
        fichero = open("datos/pedidos.csv", "w")
        for linea in lineas:
            datos = linea.strip().split(";")
            if int(datos[0]) != id_pedido:
                fichero.writelines([linea])
        fichero.close()
 
    def notificar_cliente(self, id_pedido):
        for i in range(self.__nro_pedidos):
            if self.__pedidos[i].id_pedido == id_pedido:
                pedido = self.__pedidos[i]
                if pedido.tipo == "Domicilio":
                    pedido.estado = "En camino"
                    print(f"\n  ¡{pedido.cliente.nombre}, "
                          f"tu pizza ya está en camino a {pedido.cliente.direccion}!")
                else:
                    pedido.estado = "Listo"
                    print(f"\n  ¡{pedido.cliente.nombre}, "
                          "tu pizza está lista! Puedes pasar a recogerla.")
                self.__pizzas_en_prod = self.__pizzas_en_prod - pedido.nro_pizzas
                return
        print(f"  Pedido #{id_pedido} no encontrado.")
 
    def calcular_ventas(self):
        total = 0.0
        for i in range(self.__nro_pedidos):
            total += self.__pedidos[i].total
        return total
 
    def generar_reporte(self):
        reporte = Reporte(self.__pedidos, self.__nro_pedidos)
        reporte.generar_tabla()
 
    def mostrar_catalogo(self):
        print(f"\n  Catálogo — {self.__nombre}")
        print("  " + "─" * 34)
        for i in range(self.__nro_pizzas):
            print(f"    {i + 1}. ", end="")
            self.__catalogo[i].describir()
 
    def mostrar_inventario(self):
        print(f"\n  Inventario — {self.__nombre}")
        print("  " + "─" * 50)
        for i in range(self.__nro_ing):
            self.__inventario[i].describir()
 
    def mostrar_pedidos_activos(self):
        activos = 0
        print("\n  Pedidos en preparación:")
        for i in range(self.__nro_pedidos):
            if self.__pedidos[i].estado == "preparando":
                self.__pedidos[i].describir()
                activos = activos + 1
        if activos != 0:
            return True  
        
    def get_pizza_catalogo(self, indice):
        return self.__catalogo[indice]
 
    def get_nro_pizzas_catalogo(self):
        return self.__nro_pizzas
 
    def _buscar_ingrediente(self, id_ing):
        for i in range(self.__nro_ing):
            if self.__inventario[i].id_ing == id_ing:
                return self.__inventario[i]
        return None