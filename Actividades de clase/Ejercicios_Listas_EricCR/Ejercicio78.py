#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir

lista1=["a","b","D","x","r","X",3,"h","w",2,"i"]
preguntar="s"
eliminar=""

while preguntar=="s":
    eliminar=input("Qué número quieres eliminar: ")
    if str(eliminar).isnumeric():
        if int(eliminar) in lista1:
            lista1.remove(int(eliminar))
            print("Elemento eliminado")
            print(lista1)
    else:
        print("EL valor tiene que ser un número")
    preguntar=input("Quieres introducir otro valor?: (s/n) ")

            