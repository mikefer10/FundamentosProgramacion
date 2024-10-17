'''
Programa que calcula en que tiempo alcanza un vehículo más veloz a otro más lento

Entradas:
    distanciaKilometros float -> d_km
    valocidad1 float -> v1
    valocidad2 float -> v2
Salidas:
    tiempoMinutos int -> t_m
Análisis:
   Hacemos uso de conversión de unidades y nos apoyamos de una condicional
'''
d_km = float(input("¿Qué distancia hay entre ambos vehículos (Km)?: "))
v1 = float(input("¿A qué velocidad va el vehículo 1 (Km/h)?: "))
v2 = float(input("¿A qué velocidad va el vehículo 2 (Km/h)?: "))
if v1>v2:
    t_m = (d_km/(v1-v2))*60
    t_m_red = f"{t_m:.0f}"
    print("El vehículo 1 alcanzará al vehículo 2 en",t_m_red,"minutos")
else:
    print("Recuerda que el vehículo 1 va más rápido :)")
