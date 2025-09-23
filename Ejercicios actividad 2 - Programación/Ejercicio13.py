#Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el 
#área y para calcular el volumen utiliza el operador de exponente.

LadoCubo=float(input("Introduce el lado de un cubo para calcular su área y volumen: "))

ÁreaCubo=6*(LadoCubo**2)
VolumenCubo=LadoCubo**3

print("El área del cubo es:", ÁreaCubo)
print("El volumen del cubo es:", VolumenCubo)