import numpy as np

# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Persona (clase base)
# ══════════════════════════════════════════════════════════════════════════════

class Persona:

    def __init__(self, nombre, telefono):
        self.__nombre   = nombre
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, t):
        self.__telefono = t

    def describir(self):
        print(f"  Nombre: {self.__nombre} | Tel: {self.__telefono}")


# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Cliente (hereda de Persona)
# ══════════════════════════════════════════════════════════════════════════════

class Cliente(Persona):

    def __init__(self, nombre, telefono, direccion):
        super().__init__(nombre, telefono)
        self.__direccion = direccion

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, d):
        self.__direccion = d

    def describir(self):
        super().describir()
        print(f"  Dirección: {self.__direccion}")


# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Administrador (hereda de Persona)
# ══════════════════════════════════════════════════════════════════════════════

class Administrador(Persona):

    def __init__(self, nombre, telefono, cargo):
        super().__init__(nombre, telefono)
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo
    @cargo.setter
    def cargo(self, c):
        self.__cargo = c

    def describir(self):
        super().describir()
        print(f"  Cargo: {self.__cargo}")


# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Ingrediente
# ══════════════════════════════════════════════════════════════════════════════

class Ingrediente:

    def __init__(self, id_ing, nombre, cantidad, valor_unitario, unidad, stock_minimo):
        self.__id            = int(id_ing)
        self.__nombre        = nombre
        self.__cantidad      = float(cantidad)
        self.__valor_unitario = float(valor_unitario)
        self.__unidad        = unidad
        self.__stock_minimo  = float(stock_minimo)

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
        self.__cantidad = float(c)

    @property
    def valor_unitario(self):
        return self.__valor_unitario
    @valor_unitario.setter
    def valor_unitario(self, v):
        self.__valor_unitario = float(v)

    @property
    def unidad(self):
        return self.__unidad

    @property
    def stock_minimo(self):
        return self.__stock_minimo
    @stock_minimo.setter
    def stock_minimo(self, s):
        self.__stock_minimo = float(s)

    def hay_stock(self):
        return self.__cantidad >= self.__stock_minimo

    def descontar(self, cant):
        if cant > self.__cantidad:
            print(f"  ⚠  Sin stock suficiente de '{self.__nombre}'.")
            return False
        self.__cantidad = self.__cantidad - cant
        if not self.hay_stock():
            print(f"  ⚠  Stock bajo: '{self.__nombre}' "
                  f"({self.__cantidad} {self.__unidad} restantes).")
        return True

    def describir(self):
        estado = "OK" if self.hay_stock() else "BAJO"
        print(f"  [{estado}] {self.__nombre}: "
              f"{self.__cantidad} {self.__unidad} | "
              f"${self.__valor_unitario}/u")


# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Pizza
# ══════════════════════════════════════════════════════════════════════════════

class Pizza:

    def __init__(self, id_pizza, nombre, precio_venta):
        self.__id          = int(id_pizza)
        self.__nombre      = nombre
        self.__precio_venta = float(precio_venta)
        # Arreglos paralelos: ingredientes y cantidades requeridas
        self.__ingredientes = np.full([10], fill_value=None, dtype=object)
        self.__cantidades   = np.zeros(10, dtype=float)
        self.__nro_ing      = 0

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
        self.__nro_ing = self.__nro_ing + 1

    def verificar_ingredientes(self):
        for i in range(self.__nro_ing):
            ing  = self.__ingredientes[i]
            cant = self.__cantidades[i]
            if ing.cantidad < cant:
                print(f"  ✗ Sin ingrediente: '{ing.nombre}' "
                      f"(necesita {cant} {ing.unidad}, hay {ing.cantidad}).")
                return False
        return True

    def descontar_ingredientes(self):
        for i in range(self.__nro_ing):
            self.__ingredientes[i].descontar(self.__cantidades[i])

    def calcular_costo(self):
        costo = 0.0
        for i in range(self.__nro_ing):
            costo = costo + (self.__ingredientes[i].valor_unitario * self.__cantidades[i])
        return costo

    def describir(self):
        print(f"  {self.__nombre} — ${self.__precio_venta:,.0f}")


# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Pedido
# ══════════════════════════════════════════════════════════════════════════════

class Pedido:

    _contador = 1

    def __init__(self, id_pedido, cliente, tipo):
        self.__id      = int(id_pedido)
        self.__cliente = cliente
        self.__tipo    = tipo          # LOCAL o DOMICILIO
        self.__estado  = "Preparando"  # Preparando | Listo | En camino
        self.__total   = 0.0
        self.__pizzas  = np.full([10], fill_value=None, dtype=object)
        self.__nro_pizzas = 0

    @property
    def id_pedido(self):
        return self.__id

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
        self.__nro_pizzas = self.__nro_pizzas + 1

    def calcular_total(self):
        self.__total = 0.0
        for i in range(self.__nro_pizzas):
            self.__total = self.__total + self.__pizzas[i].precio_venta
        return self.__total

    def get_pizza(self, i):
        return self.__pizzas[i]

    def describir(self):
        nombres = ""
        for i in range(self.__nro_pizzas):
            nombres = nombres + self.__pizzas[i].nombre
            if i < self.__nro_pizzas - 1:
                nombres = nombres + ", "
        print(f"  Pedido #{self.__id} | {self.__cliente.nombre} | "
              f"{self.__tipo} | {self.__estado} | "
              f"Pizzas: {nombres} | Total: ${self.__total:,.0f}")


# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Reporte
# ══════════════════════════════════════════════════════════════════════════════

class Reporte:

    def __init__(self, pedidos, nro_pedidos):
        self.__pedidos     = pedidos
        self.__nro_pedidos = nro_pedidos
        self.__total_ventas = 0.0
        self.__costo_total  = 0.0

    @property
    def total_ventas(self):
        return self.__total_ventas

    @property
    def costo_total(self):
        return self.__costo_total

    def calcular_totales(self):
        self.__total_ventas = 0.0
        self.__costo_total  = 0.0
        for i in range(self.__nro_pedidos):
            self.__total_ventas = self.__total_ventas + self.__pedidos[i].total
            for j in range(self.__pedidos[i].nro_pizzas):
                self.__costo_total = self.__costo_total + self.__pedidos[i].get_pizza(j).calcular_costo()

    def generar_tabla(self):
        self.calcular_totales()
        ganancia = self.__total_ventas - self.__costo_total

        # Arreglos para acumular rentabilidad por pizza
        arr_nombres   = np.full([50], fill_value=None, dtype=object)
        arr_vendidas  = np.zeros(50, dtype=int)
        arr_ventas    = np.zeros(50, dtype=float)
        arr_costos    = np.zeros(50, dtype=float)
        nro_tipos     = 0

        for i in range(self.__nro_pedidos):
            for j in range(self.__pedidos[i].nro_pizzas):
                pizza  = self.__pedidos[i].get_pizza(j)
                nombre = pizza.nombre
                costo  = pizza.calcular_costo()
                precio = pizza.precio_venta

                # Buscar si ya existe en el arreglo
                encontrado = False
                for k in range(nro_tipos):
                    if arr_nombres[k] == nombre:
                        arr_vendidas[k] = arr_vendidas[k] + 1
                        arr_ventas[k]   = arr_ventas[k] + precio
                        arr_costos[k]   = arr_costos[k] + costo
                        encontrado = True
                        break

                if not encontrado:
                    arr_nombres[nro_tipos]  = nombre
                    arr_vendidas[nro_tipos] = 1
                    arr_ventas[nro_tipos]   = precio
                    arr_costos[nro_tipos]   = costo
                    nro_tipos = nro_tipos + 1

        SEP  = "═" * 68
        SEP2 = "─" * 68
        print(f"\n{SEP}")
        print(f"  REPORTE DE VENTAS")
        print(SEP)
        print(f"  Total pedidos : {self.__nro_pedidos}")
        print(f"  Total ventas  : ${self.__total_ventas:>12,.0f}")
        print(f"  Costo total   : ${self.__costo_total:>12,.0f}")
        print(f"  Ganancia neta : ${ganancia:>12,.0f}")
        print(SEP2)
        print(f"  {'Pizza':<20} {'Vendidas':>8} {'Ventas':>11} "
              f"{'Costo':>11} {'Ganancia':>11}")
        print(SEP2)
        for k in range(nro_tipos):
            gan = arr_ventas[k] - arr_costos[k]
            signo = "✓" if gan >= 0 else "✗"
            print(f"  {signo} {arr_nombres[k]:<19} {arr_vendidas[k]:>8} "
                  f"${arr_ventas[k]:>10,.0f} "
                  f"${arr_costos[k]:>10,.0f} "
                  f"${gan:>10,.0f}")
        print(SEP)


# ══════════════════════════════════════════════════════════════════════════════
#  CLASE: Pizzeria
# ══════════════════════════════════════════════════════════════════════════════

class Pizzeria:

    def __init__(self, nombre, departamento, capacidad_maxima):
        self.__nombre           = nombre
        self.__departamento     = departamento
        self.__capacidad_maxima = int(capacidad_maxima)
        self.__pizzas_en_prod   = 0

        self.__inventario  = np.full([20], fill_value=None, dtype=object)
        self.__catalogo    = np.full([10], fill_value=None, dtype=object)
        self.__pedidos     = np.full([50], fill_value=None, dtype=object)
        self.__nro_ing     = 0
        self.__nro_pizzas  = 0
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

    # ── Carga de datos desde CSV ───────────────────────────────────────────
    def cargar_ingredientes(self):
        fichero = open("ingredientes.csv", "r")
        lineas  = fichero.readlines()
        for linea in lineas:
            datos = linea.strip().split(";")
            self.__inventario[self.__nro_ing] = Ingrediente(
                datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]
            )
            self.__nro_ing = self.__nro_ing + 1
        fichero.close()
        print(f"  ✓ {self.__nro_ing} ingredientes cargados.")

    def cargar_pizzas(self):
        fichero = open("pizzas.csv", "r")
        lineas  = fichero.readlines()
        for linea in lineas:
            datos  = linea.strip().split(";")
            pizza  = Pizza(datos[0], datos[1], datos[2])
            ids    = datos[3].split("-")
            cants  = datos[4].split("-")
            for k in range(len(ids)):
                ing = self._buscar_ingrediente(int(ids[k]))
                if ing is not None:
                    pizza.agregar_ingrediente(ing, float(cants[k]))
            self.__catalogo[self.__nro_pizzas] = pizza
            self.__nro_pizzas = self.__nro_pizzas + 1
        fichero.close()
        print(f"  ✓ {self.__nro_pizzas} pizzas cargadas.")

    # ── Métodos de negocio ─────────────────────────────────────────────────
    def validar_capacidad(self):
        return self.__pizzas_en_prod < self.__capacidad_maxima

    def registrar_pedido(self, cliente, pizzas_sel, nro_sel, tipo):
        if not self.validar_capacidad():
            print(f"\n  ✗ Cocina llena ({self.__capacidad_maxima} pizzas máximo).")
            return None

        for i in range(nro_sel):
            if not pizzas_sel[i].verificar_ingredientes():
                print(f"\n  ✗ No se puede preparar '{pizzas_sel[i].nombre}'.")
                return None

        for i in range(nro_sel):
            pizzas_sel[i].descontar_ingredientes()

        pedido = Pedido(self.__nro_pedidos + 1, cliente, tipo)
        for i in range(nro_sel):
            pedido.agregar_pizza(pizzas_sel[i])
        pedido.calcular_total()

        self.__pedidos[self.__nro_pedidos] = pedido
        self.__nro_pedidos    = self.__nro_pedidos + 1
        self.__pizzas_en_prod = self.__pizzas_en_prod + nro_sel

        # Guardar pedido en CSV
        fichero = open("pedidos.csv", "a")
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

        print(f"\n  ✓ Pedido #{pedido.id_pedido} registrado — "
              f"{cliente.nombre} | ${pedido.total:,.0f}")
        return pedido

    def cancelar_pedido(self, id_pedido):
        for i in range(self.__nro_pedidos):
            if self.__pedidos[i].id_pedido == id_pedido:
                if self.__pedidos[i].estado != "Preparando":
                    print(f"  ✗ El pedido #{id_pedido} ya está "
                          f"'{self.__pedidos[i].estado}' y no puede cancelarse.")
                    return
                self.__pizzas_en_prod = self.__pizzas_en_prod - self.__pedidos[i].nro_pizzas
                # Desplazar arreglo una posición hacia atrás
                for j in range(i, self.__nro_pedidos - 1):
                    self.__pedidos[j] = self.__pedidos[j + 1]
                self.__pedidos[self.__nro_pedidos - 1] = None
                self.__nro_pedidos = self.__nro_pedidos - 1
                print(f"  ✓ Pedido #{id_pedido} cancelado.")
                return
        print(f"  ✗ Pedido #{id_pedido} no encontrado.")

    def notificar_cliente(self, id_pedido):
        for i in range(self.__nro_pedidos):
            if self.__pedidos[i].id_pedido == id_pedido:
                pedido = self.__pedidos[i]
                if pedido.tipo == "Domicilio":
                    pedido.estado = "En camino"
                    print(f"\n  🛵  ¡{pedido.cliente.nombre}, "
                          f"tu pizza ya está en camino a {pedido.cliente.direccion}!")
                else:
                    pedido.estado = "Listo"
                    print(f"\n  🍕  ¡{pedido.cliente.nombre}, "
                          "tu pizza está lista! Puedes pasar a recogerla.")
                self.__pizzas_en_prod = self.__pizzas_en_prod - pedido.nro_pizzas
                return
        print(f"  ✗ Pedido #{id_pedido} no encontrado.")

    def calcular_ventas(self):
        total = 0.0
        for i in range(self.__nro_pedidos):
            total = total + self.__pedidos[i].total
        return total

    def generar_reporte(self):
        reporte = Reporte(self.__pedidos, self.__nro_pedidos)
        reporte.generar_tabla()

    # ── Mostrar datos ──────────────────────────────────────────────────────
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
            if self.__pedidos[i].estado == "Preparando":
                self.__pedidos[i].describir()
                activos = activos + 1
        if activos == 0:
            print("  No hay pedidos en preparación.")

    def get_pizza_catalogo(self, indice):
        return self.__catalogo[indice]

    def get_nro_pizzas_catalogo(self):
        return self.__nro_pizzas

    # ── Utilidad interna ───────────────────────────────────────────────────
    def _buscar_ingrediente(self, id_ing):
        for i in range(self.__nro_ing):
            if self.__inventario[i].id_ing == id_ing:
                return self.__inventario[i]
        return None


# ══════════════════════════════════════════════════════════════════════════════
#  MENÚ — funciones de navegación
# ══════════════════════════════════════════════════════════════════════════════

def pedir_opcion(opciones):
    while True:
        try:
            valor = int(input("\n  Opción: "))
            if valor in opciones:
                return valor
            print(f"  Opción inválida. Elige entre {opciones}.")
        except ValueError:
            print("  Ingresa un número válido.")

def pausar():
    input("\n  Presiona Enter para continuar...")

def encabezado(titulo):
    sep = "═" * 44
    print(f"\n{sep}")
    print(f"  {titulo}")
    print(sep)


# ── Flujo: nuevo pedido ────────────────────────────────────────────────────

def flujo_nuevo_pedido(pizzeria):
    encabezado("NUEVO PEDIDO")

    nombre = input("  Nombre del cliente: ").strip()
    if nombre == "":
        print("  El nombre es obligatorio.")
        return

    print("\n  Tipo de pedido:")
    print("    1. Local")
    print("    2. Domicilio")
    tipo_op = pedir_opcion([1, 2])

    if tipo_op == 1:
        tipo      = "Local"
        telefono  = ""
        direccion = "Local"
    else:
        tipo      = "Domicilio"
        telefono  = input("  Teléfono: ").strip()
        direccion = input("  Dirección: ").strip()
        if direccion == "":
            print("  La dirección es obligatoria para domicilio.")
            return

    cliente = Cliente(nombre, telefono, direccion)

    pizzeria.mostrar_catalogo()

    # Arreglo de tamaño fijo para pizzas seleccionadas
    pizzas_sel = np.full([10], fill_value=None, dtype=object)
    nro_sel    = 0

    while True:
        print(f"\n  Agregar pizza (0 para terminar):")
        try:
            num = int(input("  Número: "))
        except ValueError:
            continue

        if num == 0:
            if nro_sel == 0:
                print("  Debes seleccionar al menos una pizza.")
                continue
            break

        if 1 <= num <= pizzeria.get_nro_pizzas_catalogo():
            pizzas_sel[nro_sel] = pizzeria.get_pizza_catalogo(num - 1)
            print(f"  + {pizzas_sel[nro_sel].nombre} agregada.")
            nro_sel = nro_sel + 1
        else:
            print(f"  Número inválido.")

    pizzeria.registrar_pedido(cliente, pizzas_sel, nro_sel, tipo)


# ── Flujo: marcar listo ────────────────────────────────────────────────────

def flujo_marcar_listo(pizzeria):
    encabezado("MARCAR PEDIDO LISTO")
    pizzeria.mostrar_pedidos_activos()
    try:
        id_p = int(input("\n  ID del pedido listo: "))
        pizzeria.notificar_cliente(id_p)
    except ValueError:
        print("  ID inválido.")


# ── Flujo: cancelar pedido ─────────────────────────────────────────────────

def flujo_cancelar_pedido(pizzeria):
    encabezado("CANCELAR PEDIDO")
    pizzeria.mostrar_pedidos_activos()
    try:
        id_p = int(input("\n  ID del pedido a cancelar: "))
        pizzeria.cancelar_pedido(id_p)
    except ValueError:
        print("  ID inválido.")


# ── Menú administración ────────────────────────────────────────────────────

def menu_administracion(pizzeria, admin):
    while True:
        encabezado(f"ADMINISTRACIÓN — {admin.nombre}")
        print("  1. Ver inventario")
        print("  2. Ver pedidos activos")
        print("  3. Generar reporte de ventas")
        print("  4. Ver catálogo")
        print("  5. Ver total de ventas del día")
        print("  0. Volver")
        opcion = pedir_opcion([0, 1, 2, 3, 4, 5])

        if opcion == 1:
            pizzeria.mostrar_inventario()
        elif opcion == 2:
            pizzeria.mostrar_pedidos_activos()
        elif opcion == 3:
            pizzeria.generar_reporte()
        elif opcion == 4:
            pizzeria.mostrar_catalogo()
        elif opcion == 5:
            total = pizzeria.calcular_ventas()
            print(f"\n  Total ventas del día: ${total:,.0f}")
        elif opcion == 0:
            break
        pausar()


# ══════════════════════════════════════════════════════════════════════════════
#  ALGORITMO PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

pizzeria = Pizzeria("La Bella Napoli", "Bogotá D.C.", 10)
admin    = Administrador("Carlos", "3001234567", "Gerente")

print("\n  Cargando datos...")
pizzeria.cargar_ingredientes()
pizzeria.cargar_pizzas()
pausar()

while True:
    encabezado(f"🍕  {pizzeria.nombre}  |  {pizzeria.departamento}")
    print(f"  Pizzas en producción: "
          f"{pizzeria.pizzas_en_prod} / {pizzeria.capacidad_maxima}")
    print()
    print("  1. Nuevo pedido")
    print("  2. Marcar pedido como listo")
    print("  3. Cancelar pedido")
    print("  4. Panel de administración")
    print("  0. Salir")

    opcion = pedir_opcion([0, 1, 2, 3, 4])

    if opcion == 1:
        flujo_nuevo_pedido(pizzeria)
    elif opcion == 2:
        flujo_marcar_listo(pizzeria)
    elif opcion == 3:
        flujo_cancelar_pedido(pizzeria)
    elif opcion == 4:
        menu_administracion(pizzeria, admin)
    elif opcion == 0:
        print("\n  ¡Hasta luego!\n")
        break

    pausar()