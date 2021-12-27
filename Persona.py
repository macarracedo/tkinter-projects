class Persona:

    def __init__(self, nombre, dni, edad=None):
        self._nombre=nombre
        self._dni=dni
        self._edad=edad


    @property
    def edad(self):
        """Propiedad edad"""
        return self._edad

    @edad.setter
    def edad(self, value):
        if value > 0:
            self._edad = value
        else:
            self._edad = 0

    @edad.deleter
    def edad(self):
        del self._edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,value):
        self._nombre=value

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self,value):
        self._dni = value

    @dni.deleter
    def dni(self):
        del self._dni

    def mostrar(self):
        return "Datos de persona: Nombre: {0}, DNI: {1}, Edad: {2}.".format(self.nombre, self.dni, self.edad)

    def esMayorDeEdad(self):
        toret=False
        if self.edad > 18:
            toret=True
        return toret

    def __str__(self):
        return "\n   Nombre: {}\n   Dni: {}\n   Edad {}".format(self.nombre, self.dni, self.edad)
