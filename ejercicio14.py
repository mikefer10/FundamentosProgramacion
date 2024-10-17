'''
Programa que recibe un número de dos cifras y mustra el número invertido

Entradas:
    numero int -> num
Salidas:
    numeroInvertido int -> num_i
Análisis:
   Hacemos uso únicamente de operaciones básicas
'''
num = str(input("Ingresa un número de dos cifras: "))
c1 = int(num)//10
c2 = int(num)-(c1*10)
if int(num)%10 == 0:
    arreglo = "0"+str(c1)
    num_i = (c2*10)+c1
else:
    num_i = (c2*10)+c1

if int(num) >= 100 or num_i >= 100:
    print("Por favor ingresa un número de dos cifras")
elif int(num)%10 == 0:
    print("El inverso de "+num+" es "+arreglo)
else:
    print("El inverso de "+num+" es "+str(num_i))