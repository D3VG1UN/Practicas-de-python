#Programa que pida un número de horas y muestre por pantalla 
#los minutos y segundos

horas=int(input("Introduce las horas que quieres que convierta en minutos y segundos: "))

minutos=horas*60
segundos=horas*3600

print(f"{horas} hora/s equivalen a {minutos} minutos y {segundos} segundos")