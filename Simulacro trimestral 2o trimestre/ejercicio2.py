contrasenas=input("Introduce las contraseñas separadas por guiones: ").split("-")

contra_segura=[]
contra_debil=[]
contra_invalida=[]

nums=0
letras=0
simbolos=0

contra_mas_larga=""

for i in contrasenas:
    nums=0
    letras=0
    simbolos=0

    if int(len(i))>len(contra_mas_larga):
        contra_mas_larga=i
      
    for x in range (len(i)):
        if i[x].isalpha():
           letras+=1
        elif i[x].isnumeric():
           nums+=1
        else:
          simbolos+=1

    if len(i)>=8 and nums>=1 and letras>=1:
        contra_segura.append(i)

    if len(i)<8:
        contra_debil.append(i)
    elif nums==0 or letras==0 and not i in contra_debil:
        contra_debil.append(i)
    elif simbolos>=1:
        contra_invalida.append(i)

print("Contraseñas seguras:",contra_segura)
print("Contraseñas débiles:",contra_debil)
print("Contraseñas inválidas:",contra_invalida)
print("Contraseña más larga:",contra_mas_larga)