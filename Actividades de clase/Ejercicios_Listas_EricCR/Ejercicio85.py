#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos

listaingles=[]
listacaste=[]
listacata=[]
pediralumno="s"
alumno=""
notaingles=0
notacaste=0
notacata=0
cantidadalumnos=0

while pediralumno=="s":
    cantidadalumnos+=1
    alumno=input("Introduce el nombre del alumno: ")
    notaingles=float(input("Nota inglés: "))
    listaingles.append(notaingles)
    notacaste=float(input("Nota castellano: "))
    listacaste.append(notacaste)
    notacata=float(input("Nota catalán: "))
    listacata.append(notacata)

    pediralumno=input("Desea introducir otro estudiante? (s/n): ")

print("")
listacata.sort()
listacaste.sort()
listaingles.sort()
print("Inglés:",listaingles)
print("Castellano:",listacaste)
print("Catalán:",listacata)

print("")
mediaingles=round(sum(listaingles)/cantidadalumnos,1)
print(f"La media en inglés es: {mediaingles}")
mediacaste=round(sum(listacaste)/cantidadalumnos,1)
print(f"La media en castellano es: {mediacaste}")
mediacata=round(sum(listacata)/cantidadalumnos,1)
print(f"La media en catalán es: {mediacata}")

lenlistaingles = len(listaingles)
lenlistacaste = len(listacaste)
lenlistacata = len(listacata)

print("")
if lenlistaingles % 2 == 0:
    medianalistaingles = (listaingles[lenlistaingles//2 - 1] + listaingles[lenlistaingles//2]) / 2
else:
    medianalistaingles = listaingles[lenlistaingles//2]

if lenlistacaste % 2 == 0:
    medianalistacaste = (listacaste[lenlistacaste//2 - 1] + listacaste[lenlistacaste//2]) / 2
else:
    medianalistacaste = listacaste[lenlistacaste//2]

if lenlistacata % 2 == 0:
    medianalistacata = (listacata[lenlistacata//2 - 1] + listacata[lenlistacata//2]) / 2
else:
    medianalistacata = listacata[lenlistacata//2]

print(f"La mediana de inglés es: {medianalistaingles}")
print(f"La mediana de castellano es: {medianalistacaste}")
print(f"La mediana de catalán es: {medianalistacata}")