#Programació del projecte password - criteri C.

print("INSTRUCCIONES:")
print("1. La longitud del password tiene que tener entre 6 y 8 caracteres.")
print("2. Forzar los siguientes valores según la posición indicada: ")
print("     Posición 1: Un número mayor o igual que 1 y menor o igual que 5")
print("     Posición 2: Una letra minúscula")
print("     Posición 3: Una letra mayúscula")
print("     Posición 4: Uno de los siguientes símbolos *, _, @")
print("     Posición 5: Una letra minúscula")
print("     Posición 6: Un número mayor o igual que 6 y menor o igual que 9")
print("     Posición 7: Uno de los siguientes símbolos &, /, #")
print("     Posición 8: Un número menor o igual que 5")

password=str(input("Introduce una palabra clave: "))
lonpassword=len(password)

if lonpassword>=6 and lonpassword<=8:
    if password[0]>="1" and password[0]<="5":
        print("Bienbien")
    else:
        print("Error en el caracter 1")
else:
    print(f"Error, el password tiene una longitud de {lonpassword} caracteres y no cumple los requisitos.")