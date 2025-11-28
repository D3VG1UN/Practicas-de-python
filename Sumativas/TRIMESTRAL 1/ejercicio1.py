#actividad 1. Visualizar por pantalla todos los valores que están entre dos números introducidos por teclado.

concatenar=""
var_min=int(input("Introduce el inicio: "))
var_max=int(input("Introduce el fin: "))
var_intervalo=int(input("Introduce el intervalo: "))

#He añadido un +1 ya que, como el último número se excluye, no cuenta todos los números (como en en el ejemplo, que el output
#es 1,4,7,10 - sin el +1 no sale el 10).
for i in range (var_min, var_max + 1, var_intervalo):
    concatenar= concatenar + str(i) + ","

#para que no salga la última coma y se respete el formato de salida
print(concatenar[:-1])