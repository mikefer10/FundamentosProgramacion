'''
Programa que pide al usuario 2 coordenadas y mustra su diferencia

Entradas:
    coordenadaX1 int -> x1
    coordenadaY1 int -> y1
    coordenadaX2 int -> x2
    coordenadaY2 int -> y2
Salidas:
    diferencia int -> dif
Análisis:
   Ubicamos la posición entre las dos coordenadas y el espacio que hay en ellos
'''
import math
x1 = int(input("Ingresa X1: "))
y1 = int(input("Ingresa Y1: "))
x2 = int(input("Ingresa X2: "))
y2 = int(input("Ingresa Y2: "))
dif = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
dif_red = f"{dif:.0f}"
print("La distancia que hay entre "+str(x1)+","+str(y1)+" y "+str(x2)+","+str(y2)+" es: "+str(dif_red))