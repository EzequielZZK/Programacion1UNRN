# Ejercicio 3
# Armar una nueva lista con nombres normalizados

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]

nombres_normalizados = []

for nombre in nombres:
    lista_nombres = nombre.strip().capitalize()
    nombres_normalizados.append(lista_nombres)

print(nombres_normalizados)