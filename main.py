import sys
import os
 
sys.path.insert(0, os.path.dirname(__file__))
 
from modelos.pizzeria import Pizzeria
from modelos.administrador import Administrador
from menu.menu import menu_principal, pausar
 
# algoritmo principal
 
pizzeria = Pizzeria("La Bella Napoli", "Bogotá D.C.", 10)
admin    = Administrador("Anderson", "3001234567", "Gerente")
 
print("\n  Cargando datos...")
pizzeria.cargar_ingredientes()
pizzeria.cargar_pizzas()
pausar()
 
menu_principal(pizzeria, admin)