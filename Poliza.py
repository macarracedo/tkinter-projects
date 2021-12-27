from Cliente import Cliente
import json
from datetime import datetime

# DDMMAA_HMS
from Vivienda import Vivienda


class Poliza:

    def __init__(self, cliente, vivienda):
        self._num_poliza=self.generarNumPoliza(cliente.dni,vivienda.refCatastral)
        self._cliente=cliente
        self._vivienda=vivienda
        self._fecha_creacion=datetime.now().strftime("%d/%m/%Y")

    @property
    def num_poliza(self):
        return self._num_poliza

    @property
    def cliente(self):
        return self._cliente

    @property
    def vivienda(self):
        return self._vivienda

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    """
        Genera un numero único para cada relacion cliente-vivienda.
    """
    def generarNumPoliza(self, dni, refCatastral):
        toret = dni
        toret += "_"
        toret += refCatastral
        # dni_refCatatral
        return toret

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return "Cliente: {}\nVivienda: {}\nNum. póliza: {}\nFecha de creación: {}".format(self.cliente,self.vivienda,self.num_poliza,self.fecha_creacion)

if __name__ == "__main__":
    print(40 * "+")
    cliente1 = Cliente("Pedro","35588957e",21)
    vivienda1 = Vivienda("FS66SS82NCIQP898QN", 245,36000)
    poliza1 = Poliza(cliente1,vivienda1)
    print(poliza1)
    print(40 * "+")