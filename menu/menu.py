import numpy as np
from modelos.cliente import Cliente
from modelos.administrador import Administrador
 
 
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
 
 
# Flujo: nuevo pedido 
 
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
 
    pizzas_sel = np.full([10], fill_value=None, dtype=object)
    nro_sel = 0
 
    while True:
        print(f"\n  Agregar pizza (0 para terminar):")
        try:
            num = int(input("  Número: "))
        except ValueError:
            continue
 
        if num == 0:
            if nro_sel == 0:
                break
                # print("  Debes seleccionar al menos una pizza.")
                # continue
            break
 
        if 1 <= num <= pizzeria.get_nro_pizzas_catalogo():
            pizzas_sel[nro_sel] = pizzeria.get_pizza_catalogo(num - 1)
            print(f"  + {pizzas_sel[nro_sel].nombre} agregada.")
            nro_sel = nro_sel + 1
        else:
            print(f"  Número inválido.")
    
    if nro_sel >=1 : 
        pizzeria.registrar_pedido(cliente, pizzas_sel, nro_sel, tipo)
 
 
# Flujo: marcar listo 
 
def flujo_marcar_listo(pizzeria):
    encabezado("MARCAR PEDIDO LISTO")
    pizzeria.mostrar_pedidos_activos()
    try:
        id_p = int(input("\n  ID del pedido listo: "))
        pizzeria.notificar_cliente(id_p)
    except ValueError:
        print("  ID inválido.")
 
 
# Flujo: cancelar pedido 
 
def flujo_cancelar_pedido(pizzeria):
    encabezado("CANCELAR PEDIDO")
    if pizzeria.mostrar_pedidos_activos():
        try: 
            id_p = int(input("\n ID del pedido a cancelar: "))
            pizzeria.cancelar_pedido(id_p)
            pizzeria._eliminar_pedido_csv(id_p)
        except ValueError: 
            print("  ID inválido.")
    else:
        print("No hay pedidos")

    # try:
    #     id_p = int(input("\n  ID del pedido a cancelar: "))
    #     pizzeria.cancelar_pedido(id_p)
    # except ValueError:
    #     print("  ID inválido.")
 
 
# Menú administración 
 
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
            print(f"\n  Total ventas del día: ${total}")
        elif opcion == 0:
            break
        pausar()
 
 
# Menú principal 
 
def menu_principal(pizzeria, admin):
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