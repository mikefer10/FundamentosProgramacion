'''
Programa que calcula la suma, resta, multplicación y división de 2 números

Entradas: 
    numero1 int -> n1
    numero2 int -> n2
Salidas:
    suma int -> sum
    resta int -> res
    multiplicación int -> multi
    división float -> div
Análisis:
    Usamos los operadores aritméticos básicos
'''
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
sum = n1+n2
res = n1-n2
multi = n1*n2
div = float(n1/n2)
div_red = f"{div:.1f}"
print("Operando los números tenemos que: \n",n1," + ",n2," = ",sum,"\n",n1," - ",n2," = ",res,"\n",n1," x ",n2," = ",multi,"\n",n1," ÷ ",n2," = ",div)
