#Programa un código que permita contar el número de vocales de la siguiente frase: No 
#hay mal que dure cien años

frase=str("No hay mal que dure cien años")

cantidad_a=frase.count("a")
cantidad_e=frase.count("e")
cantidad_i=frase.count("i")
cantidad_o=frase.count("o")
cantidad_u=frase.count("u")

print(f"El número de a es {cantidad_a} el número de e es {cantidad_e} el número de i es {cantidad_i} el número de o es {cantidad_o} y el número de u es {cantidad_u}")