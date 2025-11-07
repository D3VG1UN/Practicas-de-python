# Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.

notas=int(input("Introduce las notas que quieres introducir: "))

for i in range (notas):
    nota=float(input("Introduce una nota: "))
    if nota>5:
        print("Asignatura aprobada")
    else:
        print("Asignatura suspendida")