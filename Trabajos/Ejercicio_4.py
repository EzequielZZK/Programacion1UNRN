#Ejercicio 4 - Edad valida

edad_valida = input("Ingrese su edad: ").strip()

if edad_valida.isnumeric():

    edad = int(edad_valida)

    if edad >= 0 and edad <= 120:
        print("Edad cargada:", edad)

    else:
        print("Error: edad fuera de rango establecido")

else:
    print("Error: debe ingresar un numero valido")