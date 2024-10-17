'''
Programa que recibe dos variables y las intercambia

Entradas:
    variableA int -> a
    variableB int -> b
Salidas:
    mensaje str -> men
Análisis:
   Hacemos uso de una doble asignación de variables (en tiempo de ejecución)
'''
a = int(input("¿Cuánto quieres que valga A?: "))
b = int(input("¿Cuánto quieres que valga B?: "))
a_nueva = b
b_nueva = a
a=a_nueva
b=b_nueva
print("Ahora A = "+str(a)+" y B = "+str(b))
