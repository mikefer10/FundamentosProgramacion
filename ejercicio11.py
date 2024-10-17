'''
Programa que pide al usuario 2 números y mustra la separación entre ellos

Entradas:
    numero1 int -> n1
    numero2 int -> n2
Salidas:
    valorAbsoluto int -> v_a
Análisis:
    El valor simpre tiene que ser positivo
'''
n1 = int(input("Ingresa el número 1: "))
n2 = int(input("Ingresa el número 2: "))
if n1 > n2:
    v_a = n1-n2
else: 
    v_a = n2-n1

print("Entre "+str(n1)+" y "+str(n2)+" hay "+str(v_a)+" números de separación")