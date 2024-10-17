'''
Programa que convierte Grados Fehrenheit a Grados Celsius 

Entradas: 
    gradosFarhenheit int -> g_f
Salidas:
    grdosCelsius int -> g_c
Análisis:
    Usamos los operadores aritméticos básicos
'''
g_f = int(input("Ingrsa los grados en la Escala Fahrenheit: "))
g_c = (g_f-32)/(1.8)
g_c_red = f"{g_c:.2f}"
mensaje = str(g_f)+ "°F son "+str(g_c_red)+"°C"
print(mensaje)