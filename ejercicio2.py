'''
Programa que calcule el area y el perímetro
de u  rectángulo a partir de su base y cu altura
Entradas:
    base: integer
    altura: intrger
Slidas:
    perimetro: integer
    area: integer 
'''
base = input("Ingresa el valor de la base: ")
base = int(base)
altura = input("Ingresa el valor de la altura: ")
altura = int(altura)
area = base*altura
perimetro = (base + altura) * 2
#Mensaje forma 1
mensaje = "La área es de " + str(area) + " y el perímetro es de " + str(perimetro)
print(mensaje)
#Mensaje forma 2
mensaje = "La área es de ", area,  "y el perímetro es de ", perimetro
print(mensaje)

