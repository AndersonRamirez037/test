from models.pizzeria import Pizzeria
from models.pedido import Pedido
from models.pizza import Pizza

pizzeria = Pizzeria("Fast Pizza")

while True:
    print("\n1. Crear pedido")
    print("2. Ver reporte")
    print("3. Salir")

    op = int(input("Opcion: "))

    if op == 1: 
        pedido = Pedido(1, "2025-01-01", "PREPARANDO")

        pizza = Pizza(1, "Hawaiana", "Piña y jamón", 1, 2000)
        pedido.agregarPizza(pizza)
        pedido.calcularTotal()

        pizzeria.registrarPedido(pedido)

        print("Pedido Creado ")

    elif op == 2:
        pizzeria.generarReporte()

    elif op == 3:
        break

