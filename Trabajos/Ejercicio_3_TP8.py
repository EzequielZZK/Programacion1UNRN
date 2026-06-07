# Ejercicio 3 — Base de datos de alumnos

alumnos = []

for i in range(4):

    nombre = input("Ingrese un nombre: ").strip()

    if nombre != "":
        alumnos.append(nombre)

archivo = open("alumnos.txt", "w")

for alumno in alumnos:
    archivo.write(alumno + "\n")

archivo.close()