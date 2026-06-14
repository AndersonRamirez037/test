from modelos.persona import Persona

class Administrador(Persona):
    def __init__(self, nombre, telefono, cargo):
        super().__init__(nombre, telefono)
        self.__cargo = cargo

    def describir(self):
        return f"{super().__str__()}, Cargo: {self.__cargo}" 