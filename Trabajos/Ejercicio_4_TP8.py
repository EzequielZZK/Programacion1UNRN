# Ejercicio 4 — Lectura de archivo

temperaturas = {}
archivo = open("temperaturas.txt", "r")

for linea in archivo:

    ciudad, temperatura = linea.strip().split(";")

    if ciudad not in temperaturas:
        temperaturas[ciudad] = []

    temperaturas[ciudad].append(int(temperatura))

archivo.close()

print(temperaturas)