"""
Dirección de la oficina
Num telefono
Num trabajadores.
"""
import json
import pickle
import sys

from Cliente import Cliente
from Poliza import Poliza
from Vivienda import Inmueble, Vivienda


class Oficina:

    def __init__(self, direccion=None, tlf=None, num_empleados=None):
        self._dict = dict()
        self._direccion = direccion
        self._tlf = tlf
        self._num_empleados = num_empleados


    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = list(value)

    @direccion.deleter
    def direccion(self):
        del self._direccion

    @property
    def tlf(self):
        return self._tlf

    @tlf.setter
    def tlf(self, value):
        self._tlf = value

    @tlf.deleter
    def tlf(self):
        del self._tlf

    @property
    def num_empleados(self):
        return self._num_empleados

    @num_empleados.setter
    def num_empleados(self, value):
        self._num_empleados = value

    @num_empleados.deleter
    def num_empleados(self):
        del self._num_empleados

    """
        Si no existe la clave, crea el par clave-valor. Si existe, lo actualiza (update)
    """
    def addPair(self, poliza):
        self._dict.update({poliza.num_poliza: poliza})
        self.saveJSON()

    """
        Elimina el par cliente-vivienda dado el cliente
    """
    def delPair(self, num_poliza):
        self._dict.pop(num_poliza)
        self.saveJSON()

    """
        Devuelve el par con la clave indicada
    """
    def getPair(self,num_poliza):
        return self._dict.get(num_poliza)


    def getItems(self):
        return self._dict.items()

    """
        Elimina el último par clave-valor insertado 
    """
    def delLastPair(self):
        self._dict.popitem()
        self.saveJSON()

    def printDict(self):
        toret = ""
        for x, y in self._dict.items():
            #print(x, y)
            toret += "\n[{0} : {1}]".format(x,y)
            toret += ("\n"+40*"*")
        return toret

    def saveJSON(self, fn="data.json"):
        print("Intentando guardar el json...")
        x = self.toJSON()
        f = open(fn, "w")
        json.dump(x, f)
        f.seek(0)
        f.close

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def saveJSON_1(self, fn='data.json'):
        with open(fn, 'w') as fp:
            json.dump(self._dict, fp, indent=4)


    def loadJSON(self,fn="data.json"):
        error = True
        while error:
            try:
                print("Cargando datos de polizas desde "+fn)
                with open(input(fn)) as f:
                    self = json.load(f)
                    error = False
            except:
                print("Unexpected exception happened!!!", sys.exc_info())
                raise

    def __str__(self):
        toret = "Información de la oficina: Direccion: {0} Teléfono: {1} Num. Empleados: {2}." \
            .format(self.direccion, self.tlf, self.num_empleados)
        # if len(self.listAsegurados) > 0:
        #     toret += "\n\tAsegurados: \n"
        #     toret += "\n".join(str(e) for e in self.listAsegurados)
        # else:
        #     toret += "\nLa oficina no cuenta con asegurados asociados."
        if len(self._dict) > 0:
            toret += "\n\tPares del diccionario: \n"
            #toret += "\n".join(str(x) for x, y in self._dict.items())
            #toret += "\n".join(str(y) for x, y in self._dict.items())
            toret += self.printDict()
        else:
            toret += "\nLa oficina no cuenta con asegurados asociados."
        return toret



if __name__ == "__main__":
    oficina1 = Oficina("Calle El Paseo, n2, Bajo C","988333668",5)
    print(oficina1)
    print(40*"+")
    cliente1 = Cliente("Pedro", "35588957e", 21)
    vivienda1 = Vivienda("FS66SS82NCIQP898QN", 245, 36000)
    poliza1 = Poliza(cliente1, vivienda1)
    oficina1.addPair(poliza1)
    print(oficina1)
    print(40 * "+")
    cliente2 = Cliente("Jose", "27788345E", 24)
    vivienda2 = Vivienda("ADNJNWC86S78E9V79WD", 245, 36000)
    poliza2 = Poliza(cliente2, vivienda2)
    oficina1.addPair(poliza2)
    print(oficina1)


