# Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif

frase=input("Introduce una frase: ")
longitudFrase=len(frase)

if longitudFrase<11:
    print("La frase tiene menos de 11 caracteres.")
elif longitudFrase==11:
    print("La frase tiene 11 caracteres.")
elif longitudFrase>11:
    print("La frase tiene 11 o más caracteres.")
#Creo que podría haber usado simplemente un "else", pero he preferido usar elif.