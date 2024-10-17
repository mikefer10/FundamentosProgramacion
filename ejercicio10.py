'''
Programa que calcula la calificación final de un alumno

Entradas:
    calificacion1 float -> cal1
    calificacion2 float -> cal3
    calificacion3 float -> cal3
    calificacionExamen float -> cal_exam
    calificacionTrabajo float -> cal_t
Salidas:
    calificacionFinal float -> cal_f
Análisis:
    Usamos la suma de los porcentajes de 55%, 30% y 15% respctivamente para dar con un total de 100%
'''
cal1 = float(input("¿Cuanto sacaste en el primer parcial?: \n"))
cal2 = float(input("¿Cuanto sacaste en el segundo parcial?: \n"))
cal3 = float(input("¿Cuanto sacaste en el tercer parcial?: \n"))
cal_exam = float(input("¿Cuanto sacaste en el examen?: \n"))
cal_t = float(input("¿Cuanto sacaste en el trabajo final?: \n"))
p_p = (cal1+cal2+cal3)/3
p1 = (5.5*p_p)/10
p2 = (3*cal_exam)/10
p3 = (1.5*cal_t)/10
cal_f = p1+p2+p3
cal_f_red = f"{cal_f:.1f}"
print("Considerando la ponderación tienes "+str(cal_f_red)+" de calificación")

