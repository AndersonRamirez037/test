class Reporte():
    def __init__(self):
        self.__totalVentas = 0

    def calcularGanancias(self, pedidos):
        total = 0
        for p in pedidos:
            if p is not None:
                total += p.calcularTotal()

        self.__totalVentas = total 
        return total 

    def generarTablas(self):
        print("Generando tablas")