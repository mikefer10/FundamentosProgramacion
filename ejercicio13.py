'''
Programa que lee un número y obtiene su raíz cuadrada y raíz cúbica

Entradas:
    numero int -> num
Salidas:
    raizCuadrada float -> r2
    raizCubica float -> r3
Análisis:
   Hacemos uso de la inversa de la radicación que es la potenciación 
'''
num = int(input("Ingresa el número: "))
r2 = num**(1/2)
r2_red = f"{r2:.1f}"
r3 = num**(1/3)
r3_red = f"{r3:.1f}"
print("Del número "+str(num)+"\nRaíz cuadrada: "+str(r2_red)+"\nRaíz cúbica: "+str(r3_red))