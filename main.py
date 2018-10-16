from operaciones import *

archivo = open('lista.txt', 'r')
leer_fila = archivo.readlines()
archivo.close()

b=len(leer_fila)

print("\n1.- ordenamiento de nombres: ")
print ("2.-Busqueda de nombres")
opcion=int(input("seleccione una opcion: "))
i = 0
if opcion==1:
    print(ordenamiento(leer_fila,b,i))
elif opcion==2:
    pal = input("ingrese un nombre: ")
    busqueda(leer_fila, b, pal)
    if busqueda(leer_fila, b, pal) == True:
        print("Si se encunetra " + pal)
    else:
        print("no se encunetra " + pal)

else:
    print("Opcion incorrecta...")
