'''
Programa que calcula la hipotenusa a partir de dos catetos

Entradas: 
    catetoA int -> a
    catetoB int -> b
Salidas:
    hipotenusa float -> c
Análisis:
    Usamos el teorema de Pitágoras
'''
import math
a = int(input('Escibe el valor del cateto A: '))
b = int(input('Escibe el valor del cateto B: '))
'''
Podemos usar este otro método para calcular la hipotenusa:
c = (a*a + a*b)**(0.5)
'''
c = math.sqrt(a**2 + a**2)
c_red = f"{c:.2f}"
print("El valor de la hipotenusa es de",c_red)
