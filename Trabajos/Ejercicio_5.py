#Ejercicio 5 - Codigo de materia

codigo = input("Ingrese codigo: ").strip().upper()

if codigo.count("-") == 1:

    partes = codigo.split("-")

    izquierda = partes[0]
    derecha = partes[1]

    if izquierda.isalpha() and derecha.isnumeric():
        print("Codigo valido:", codigo)

    else:
        print("Error: el formato es incorrecto")

else:
    print("Error: debe tener un guion solo")