'''
Programa que recibe una cantidad de minutos y obtebnga las horas y minutos

Entradas: 
    minutosTotales int -> min_t
Salidas:
    horas int -> hrs
    minutosRestantes int -> min_res
Análisis:
    Usamos conversiones de unidades de tiempo
'''
min_t = int(input("Ingrsa la cantidad de minutos: "))
hrs = min_t//60
min_res = min_t-(hrs*60)
print("Si sonvertimos, "+str(min_t)+" minutos equivale a:\n"+str(hrs)+" horas con "+str(min_res)+" minutos")