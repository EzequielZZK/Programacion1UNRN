# Ejercicio 2 — Registro de sensores

mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

ubicaciones = {}
tipos = set()

for medicion in mediciones:

    tipo, valor, ubicacion = medicion

    if ubicacion not in ubicaciones:
        ubicaciones[ubicacion] = []

    ubicaciones[ubicacion].append((tipo, valor))

    tipos.add(tipo)

print(ubicaciones)
print(tipos)