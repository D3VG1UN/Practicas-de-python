# A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10

notas=int(input("Introduce las notas que quieres introducir: "))

for i in range (notas):
    nota=float(input("Introduce una nota: "))
    if nota<5 and nota>=0:
        print("Asignatura suspendida")
    elif nota<=10 and nota>=5:
        print("Asignatura aprobada")
    else:
        print("Has introducido una nota equivocada")