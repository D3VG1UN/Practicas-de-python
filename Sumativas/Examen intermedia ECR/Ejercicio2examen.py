#Utilizamos el mismo código que antes y le añadimos o modificamos lo necesario para dividir el total entre 3.
var1=float(input("Introduce el primer número: "))
var2=float(input("Introduce el segudo número: "))

vartotal=var1 + var2
vardivisión=round(vartotal/3, 3)
#usamos round() para redondear números, con la cantidad de decimales separada por una coma

print(f"el resultado de sumar {var1} y {var2} es: ",vartotal)
print(f"El resultado de dividir {vartotal} entre 3 es: ",vardivisión)
#Añadimos otro print para enseñar el resultado de la división