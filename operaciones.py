
"""se define la clase"""

#Recursivo nombres
def ordenamiento(x,ee,z):
    x.sort()
    if z==ee:
        return ""
    else:
        print(x[z])
        return ordenamiento(x,ee,z+1)

def busqueda(lista, x,palabra):
	#compara = lista[x]
	ver = False
	if x == 0:
		return 0
	elif palabra in lista[x-1]:
		ver = True
	else:
		return busqueda(lista, x-1, palabra)
	return ver
