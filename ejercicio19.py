'''
Calcula la nota final de un estuduiante e imprime el resultado 

Entradas:
    correctas int -> c
    incorrectas int -> i
    nulas str int -> n
Salidas:
    notaFinal float -> nota_f
Análisis:
   Debemos considerar que cada buena suma 5, cada mala resta 1 y las nulas 0
'''
c = int(input("CORRECTAS: "))
i = int(input("INCORRECTAS: "))
n = int(input("NULAS: "))

nota_max = (c+i+n)*5
nota_f = (c*5)+(i*(-1))
cal = (nota_f*10)/nota_max
cal_red = f"{cal:.1f}"
print("Obtuviste "+str(nota_f)+"/"+str(nota_max)+" puntos, lo que equivale a "+str(cal_red)+" de calificación")