#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

nota=float(input("Introduce tu nota por teclado: "))

if nota<5 and nota>=0:
    print(f"Has sacado un {nota} y has suspendido")
elif nota>=5 and nota<=10:
    print(f"Has sacado un {nota} y has aprobado")
else:
    print("La nota que has introducido tiene que estar entre 1 y 10")