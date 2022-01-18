import Persona

nombre = "Dali"
edad = 20
temperatura = 36.8
sexo = 'H'

"""
print("El nombre es: ", nombre, " tiene ", edad, " años")
print(f"El nombre es: {nombre} tiene {edad} años")

n1 = int(input("Ingresa el n1: "))
n2 = int(input("Ingresa el n2: "))

suma = int(n1 + n2)

print(f"La suma es {suma}")

"""

nombre = input("Nombre de la persona: ")
edad = int(input("Edad de la persona: "))

persona = Persona.Persona(nombre, edad)
print(f"Datos de la persona, nombre {persona.getNombre()}, edad: {persona.getEdad()}")

for i in range(5):
    print(f"For ({i})", end=" | ")
