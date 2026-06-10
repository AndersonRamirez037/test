class Persona:
    def __init__(self, nombre, telefono):
        self.__nombre = nombre
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

    def __str__(self):
        return (f"Nombre: {self.__nombre}, Tel: {self.__telefono}")