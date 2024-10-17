'''
Programa que calcula el area y el perímetro de un rectángulo

Entradas:
    baseRectangulo int -> b
    alturaRectangulo int -> h
Slidas:
    perimetroRectangulo int -> p
    areaRectangulo int -> a 
'''
b = int(input("Ingresa el valor de la base: "))
h = int(input("Ingresa el valor de la altura: "))
p = (b + h) * 2
a = b*h
#Mensaje forma 1
mensaje = "El área es de " + str(a) + " y el perímetro es de " + str(p)
print(mensaje)
#Mensaje forma 2
print("El área es de",a,"y el perímetro es de",p)



