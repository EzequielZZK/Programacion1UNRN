# Ejercicio 3
# Armar una nueva lista con nombres normalizados

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]

nombres_normalizados = []

for nombre in nombres:
    nuevo_nombre = nombre.strip().capitalize()
    nombres_normalizados.append(nuevo_nombre)

print(nombres_normalizados)