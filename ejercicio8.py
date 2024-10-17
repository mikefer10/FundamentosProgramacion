'''
Programa que recibe un sueldo y calcula el total con comisión incluida

Entradas: 
    sueldoBase float -> s_base
    venta1 float -> v1
    venta2 float -> v2
    venta2 float -> v3
Salidas:
    Comision float -> c
    sueldoTotal float -> s_total
Análisis:
    Usamos conversiones de porcentajes y operaciones básicas
'''
#Solicitamos de datos al usuario
s_base = float(input("Ingrsa el sueldo base: "))
v1 = float(input("Importe de la primera venta: "))
v2 = float(input("Importe de la segunda venta: "))
v3 = float(input("Importe de la tercera venta: "))

c = 0.1 * (v1 + v2 + v3)
c_red = f"{c:.2f}"
s_total = s_base + c
s_total_red = f"{s_total:.2f}"
if s_total>s_base:
    print(":) Felicidades, tu sueldo aumentó a $"+str(s_total_red)+ "\n-> Equivalente a $"+str(s_base)+ " del salario base más $"+str(c_red)+" de comisiones");
else:
    print(":( Este mes no hiciste ninguna venta, tu sueldo se queda en $"+str(s_total_red))
