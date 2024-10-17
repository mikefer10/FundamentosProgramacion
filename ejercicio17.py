'''
Programa que calcula la hora de llegada de un ciclista de una ciudad a otra

Entradas:
    salidaHoras int -> s_h
    salidaMinutos int -> s_m
    salidaSegundos int -> s_s
    tardanzaSegundos int - t_s
Salidas:
    horaArrivo int -> h_a
Análisis:
   Logramos resolver este problema con conversiones de unidades de hrs/min/seg
'''
print("Ingresa a que hora sale el ciclista:")
s_h = int(input("Hrs: "))
s_m = int(input("Min: "))
s_s = int(input("Seg: "))

while s_h < 0 or s_h > 23 or s_m < 0 or s_m > 59 or s_s < 0 or s_s > 59:
    print("Hora de salida inválida, por favor, ingrese valores válidos")
    s_h = int(input("Hrs: "))
    s_m = int(input("Min: "))
    s_s = int(input("Seg: "))


tardanza = int(input("¿Cuánto dura el viaje (Seg)?: "))

arrivo_total_s = (s_h*3600)+(s_m*60)+s_s+tardanza
arrivo_h = arrivo_total_s/3600
arrivo_h_red = arrivo_total_s//3600

s_restantes = arrivo_total_s%3600
arrivo_m = s_restantes/60
arrivo_m_red = s_restantes//60
arrivo_s = s_restantes%60

if int(arrivo_h)<10:
    arreglo = "0"+str(arrivo_h_red)
    arrivo_h2 = arreglo
else:
    arrivo_h2 = arrivo_h_red

if int(arrivo_m)<10:
    arreglo = "0"+str(arrivo_m_red)
    arrivo_m2 = arreglo
else:
    arrivo_m2 = arrivo_m_red

if int(arrivo_s)<10:
    arreglo = "0"+str(arrivo_s)
    arrivo_s2 = arreglo
else:
    arrivo_s2 = arrivo_s

if int(arrivo_h_red)==1:
    print("Llegas a la otra ciudad a la "+str(arrivo_h2)+":"+str(arrivo_m2)+":"+str(arrivo_s2))
else:
    print("El ciclista llega a la otra ciudad a las "+str(arrivo_h2)+":"+str(arrivo_m2)+":"+str(arrivo_s2))