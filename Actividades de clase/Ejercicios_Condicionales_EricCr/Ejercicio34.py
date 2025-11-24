#Corrige los 4 errores o añade el código que necesites para que el siguiente programa se 
#ejecute correctamente

#inicializo valores a cada variable
var_numero=str(6734)
var_suma=str(0)
#obtengo su longitud
var_longitud=len(var_numero)
#sumo cada digito a partir del índice de cada posición
var_suma = int(var_numero[0]) + int(var_numero[1]) + int(var_numero[2]) + int(var_numero[3])
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
var_numero=float(var_numero)
var_suma=float(var_suma)
if var_suma % 2 == 0:
    print (f"el valor de {var_suma} es par")
else:
    print(f"el valor de {var_suma} es impar")

#Error 1 (que he encontrado): el operador necesario para comprobar si un número es par o impar es %, no //, y si es igual
#a 0, entonces es par
#Error 2: valta establecer las variables como str, tipo texto, para que el "len" las cuente.
#Error 3: al hacer la lista en la línea 10, se tiene que empezar con la posición 0, no la 1. Es decir, en este caso
#"6734", la posición 0 equivale al 6, etc.
#Error 4: para las divisiones enteras, tenemos que establecer la variable como "float", en este caso, para la variable 
#"var_suma", no puede ser ni string ni int. Lo mismo pasa con la cadena: si no le damos el valor de int, el programa lo
#cuenta como texto, por lo que no está sumando los dígitos, sino que los está juntando.

#Además, he añadido un "else", en caso de que sea impar (que no lo será en el ejercicio)