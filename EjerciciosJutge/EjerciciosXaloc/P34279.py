#ejercicio 16. añadir un segundo

num=input()
listanums=num.split()
h=int(listanums[0])
m=int(listanums[1])
s=int(listanums[2])+1

if s == 60:
    s = 0
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
#esto me lo enseñó Mangel una vez, así que he decidido intentar volver a aplicarlo
print((("0" + str(h)) if h < 10 else str(h)) + ":" + (("0" + str(m)) if m < 10 else str(m)) + ":" +(("0" + str(s)) if s < 10 else str(s)))