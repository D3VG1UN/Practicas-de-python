#Cómo comprobar si un número es decimal, porque isnumeric() no detecta los decimales, variables float.
#1.
var=3.4
#var=str(var)
#2. (mejorable)
#if "." in var:
#    print("Es decimal")

#lista=["2", ".", "6"]


#3. La mejor opción
if not var==var//1:
    print("es decimal")
else:
    print("no es decimal")


