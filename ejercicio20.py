'''
Nos dice el dinero que tenemos en euros y en céntimos

Entradas:
    monedas1e int -> m_1e
    monedas2e int -> m_2e
    monedas50c int -> m_50c
    monedas20c int -> m_20c
    monedas10c int -> m_10c
Salidas:
    cantidadEuros int -> c_e
    cantidadCentimos int -> c_c    
Análisis:
   Nos basamos de una conversión base a (Céntimos) y luego lo desprendemos en las dos denominaciones
'''
print("Cuántas monedas tienes de:")
m_1e = int(input("1 EURO: "))
m_2e = int(input("2 EUROS: "))
m_50c = int(input("50 CÉNTIMOS: "))
m_20c = int(input("20 CÉNTIMOS: "))
m_10c = int(input("10 CÉNTIMOS: "))
total_centimos = ((m_2e*200)+(m_1e*100)+(m_50c*50)+(m_20c*20)+(m_10c*10))
c_e = total_centimos//100
c_c = total_centimos-(c_e*100)
print("Usted tiene en total "+str(c_e)+" euros con "+str(c_c)+" céntimos")