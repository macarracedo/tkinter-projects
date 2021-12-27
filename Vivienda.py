from enum import Enum
Inmueble = Enum('Inmueble', 'apartamento casa bajo_comercial finca')


class Vivienda:

    def __init__(self, refCatastral, metrosCuadrados, valorCatastral):
        self.refCatastral=refCatastral
        self.metrosCuadrados = metrosCuadrados
        self.valorCatastral=valorCatastral

    @property
    def refCatastral(self):
        return self._refCatastral

    @refCatastral.setter
    def refCatastral(self, value):
        self._refCatastral = value

    @refCatastral.deleter
    def refCatastral(self):
        del self._refCatastral

    @property
    def metrosCuadrados(self):
        return self._metrosCuadrados

    @metrosCuadrados.setter
    def metrosCuadrados(self, value):
        self._metrosCuadrados = value

    @metrosCuadrados.deleter
    def metrosCuadrados(self):
        del self._metrosCuadrados

    @property
    def valorCatastral(self):
        return self._valorCatastral

    @valorCatastral.setter
    def valorCatastral(self, value):
        self._valorCatastral = value

    @valorCatastral.deleter
    def valorCatastral(self):
        del self._valorCatastral

    def __str__(self):
        toret = "\n   Superficie: {1}m2\n   Valor catastral: {2}€\n   Ref. Catastral: {0}"\
            .format(self.refCatastral, self.metrosCuadrados,self.valorCatastral)

        return toret

if __name__ == "__main__":
    print(40 * "+")
    viv1 = Vivienda("FS66SS82NCIQP898QN", 245,36000)
    print(viv1)
    print(40 * "+")
