'''
Programa que calcula la media de 3 números ingresados por el usuario 

Entradas: 
    numero1 int -> n1
    numero2 int -> n2
    numero3 int -> n3
Salidas:
    media float -> med
Análisis:
    Usamos la regla de la media o promedio
'''
n1 = int(input("Ingrsa el número 1: \n"))
n2 = int(input("Ingrsa el número 2: \n"))
n3 = int(input("Ingrsa el número 3: \n"))
med = (n1+n2+n3)/3
med_red = f"{med:.1f}"
print("Calculando tenemos que el promedio de ("+str(n1)+", "+str(n2)+", "+str(n3)+") es: "+str(med_red))