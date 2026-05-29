

*Mini TP 7 - Validación y manipulación de datos*



\#####################################################



**Responder en un archivo de texto plano (.TXT), con sus palabras.**



**¿Por qué es importante validar los datos que ingresa un usuario?**

**¿Qué hace strip y en que se diferencia de split?**

**¿Para que puede servir count cuando una linea tiene datos separados por comas o por punto y coma?**

**¿Qué problema pueden traer los espacios de mas al principio o al final de un dato?**



\#####################################################



*Ejercicio 1:*



1\) Porque si el usuario ingresa datos incorrectos puede provocar Errores en el programa.



2\) La función Strip nos deja eliminar caracteres vacíos al principio y final de la misma en cambio la función Split separa texto con un separador (,)



3)Cuenta cuantos separadores hay y al mismo tiempo verifica si el formato del texto es el correcto



4\) Puede dar Errores y que los datos no coincidan correctamente



\######################################################



Este ejercicio no es para programar. Lean el código y escriban una explicación de que hace.



linea = " mara ; programación ; 8 "



partes = linea.split(";")

nombre = partes\[0].strip().capitalize()

materia = partes\[1].strip().capitalize()

nota\_texto = partes\[2].strip()



if nota\_texto.isnumeric():

&#x20;   nota = int(nota\_texto)

&#x20;   print(f"{nombre} cursa {materia} y obtuvo {nota}")

else:

&#x20;   print("La nota no es valida")

Para orientar la explicación:



¿Qué queda guardado en partes?

¿Por que se usa strip antes de capitalize?

¿Qué dato se esta validando antes de convertirlo?

¿Qué imprimiría el programa si en lugar de 8 viniera ocho?



\######################################################



*Ejercicio 2:*



1\) Queda una lista de datos separados por punto y coma (;)



2\) Porque elimina los espacios sobrantes y acomoda el texto con Capitalize ()



3\) Se valida con \[Isnumeric()] antes de convertirla



4\) La nota no es valida porque no esta expresado en forma numérica por ejemplo imprimiría "La nota no es valida"

