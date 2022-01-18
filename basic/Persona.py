class Persona:
    nombre = ""
    edad = ""

    # Todas las funciones reciben el parametro self

    # Constructor
    def __init__(self, nom, eda):
        self.nombre = nom
        self.edad = eda

    # Getters & setters
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def setNombre(self, nom):
        self.nombre = nom

    def setEdad(self, eda):
        self.edad = eda