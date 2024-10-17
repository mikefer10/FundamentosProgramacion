'''
Programa que calcula el precio final de una compra con el 15% de descuento

Entradas:
    sumaCompra float -> s_c
Salidas:
    costoFinal float -> c_f
Análisis:
    Usamos cálculos de porcentajes y operaciones básicas
'''
s_c = float(input("¿Cuanto es la suma de tu compra?: "))
c_f = s_c - (s_c*0.15)
print("Con el decuento ahora solo debes pagar $"+str(c_f))
