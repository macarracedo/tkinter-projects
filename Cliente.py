"""
num asegurado
(oficina)

"""
from Persona import Persona
from datetime import datetime

# DDMMAA_HMS

class Cliente(Persona):

    def __init__(self, nombre, dni, edad=None):
        super().__init__(nombre,dni,edad)
        self.num_asegurado=self.generarNumAsegurado(dni)

    """
        Genera un numero único para cada asegurado. Emplea la fecha y hora actual para ello.
    """
    def generarNumAsegurado(self, dni):
        now = datetime.now()
        # ddmmaa
        toret = now.strftime("%d%m%Y_")
        toret += dni;
        # ddmmaa_dniConLetra
        return toret

    def __str__(self):
        return super().__str__()+"\n   Num. de asegurado: {}".format(self.num_asegurado)

if __name__ == "__main__":
    print(40 * "+")
    cliente1 = Cliente("Pedro","35588957e",21)
    print(cliente1)
    print(40 * "+")