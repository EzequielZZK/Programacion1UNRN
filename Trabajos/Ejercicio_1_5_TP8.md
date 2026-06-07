
Trabajo practico 8

Diccionarios y archivos

Ejercicio 1:

Lista:

Una lista permite guardar varios datos en orden. Puede tener elementos repetidos y se puede modificar.

Ejemplo: notas de alumnos.

Tupla:

Una tupla es parecida a una lista, pero una vez creada no se puede modificar.

Ejemplo: una fecha de cumpleaños.

Conjunto:

Un conjunto guarda elementos sin repetir.

Ejemplo: las materias cursadas por un estudiante.

Diccionario:

Un diccionario guarda información usando una clave y un valor.

Ejemplo: una ciudad con su temperatura.

##########################

```python

Ejercicio 5:

def limpiar(texto):
    return texto.strip().capitalize()

def es_valido(nombre):
    if len(nombre) >= 3:
        return True
    return False

nombres = [" bart ", "ED", " walter", "rick "]
validos = []

for nombre in nombres:
    nombre_limpio = limpiar(nombre)

    if es_valido(nombre_limpio):
        validos.append(nombre_limpio)

print(validos)

```

A-  ¿Qué hace el programa?

Recorre una lista de nombres, elimina espacios sobrantes, corrige las mayúsculas y guarda únicamente los nombres válidos (de 3 o más caracteres) en una nueva lista.

B-  ¿Qué hace la función limpiar?

La función elimina los espacios al principio y al final usando strip() y luego normaliza el texto usando capitalize().

Ej:

" bart " -> "Bart"

C- ¿Qué hace la función es_valido?

Verifica que el nombre tenga 3 o más caracteres.

Si tiene 3 o más devuelve:

True

Si no tiene:

False

D- ¿Qué nombres quedan almacenados en validos?

Original:
```python
[" bart ", "ED", " walter", "rick "]
```
Después de limpiar:

"Bart" - "Ed" - "Walter" - "Rick"

La Validación:     
                 
Bart → 4 letras  
Ed → 2 letras (X)
Walter → 6 letras 
Rick → 4 letras 

Entonces quedan:
```python
["Bart", "Walter", "Rick"]
```

E-  ¿Qué imprime el programa al finalizar?
```python
['Bart', 'Walter', 'Rick']  
```

