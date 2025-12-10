#Drone navigation

x=int(input("Introduce el eje x: "))
y=int(input("Introduce el eje y: "))

if x > 0:
    if y > 0:
        print("Cuadrante 1")
    elif y < 0:
        print("Cuadrante 4")
elif x < 0:
    if y > 0:
        print ("Cuadrante 2")
    elif y < 0:
        print("Cuadrante 3")