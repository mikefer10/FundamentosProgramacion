'''
Programa que pide el nombre y dos apellidos y devuelve sus iniciales

Entradas:
    nombre str -> nom
    apellidoPaterno str -> a_paterno
    apellidoMaterno str -> a_materno
Salidas:
    inicialNombre int -> inicial_1
    inicialApellidoPaterno int -> inicial_2
    inicialApellidoMaterno int -> inicial_3
Análisis:
   Para resolver este problema lo que hay que hacer es usar una función propia de Python
'''
#Capturamos los datos por teclado
nombre = str(input("Nombre: "))
a_paterno = str(input("Primer apellido: "))
a_materno = str(input("Segundo Apellido: "))
#Obtenemos la inicial del nombre
entrada1 = nombre.split()
inicial_1 = "".join(letra[0].upper() for letra in entrada1)
#Obtenemos la inicial del Apellido Paterno
entrada2 = a_paterno.split()
inicial_2 = "".join(letra[0].upper() for letra in entrada2)
#Obtenemos la inicial del Apellido Materno
entrada3 = a_materno.split()
inicial_3 = "".join(letra[0].upper() for letra in entrada3)
#Creamos el mensaje
mensaje = (inicial_1+inicial_2+inicial_3)
#Imprimimos el mensaje
print("Tu nombre abreviado es:",mensaje)