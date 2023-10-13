#Um suíno, na fase de creche, ganha 30 gramas por dia. Qual é o ganho de massa por unidade de tempo, em miligramas por segundo?R: 0,3472 mg/s

#dados 
ganho_de_massa_dia = 30 # 30 gramas por dia

#O ganho de massa por unidade de tempo em miligramas por segundo pode ser calculado da seguinte forma:
ganho_de_massa_segundo = ganho_de_massa_dia / (24 * 60 * 60) #  gramas do dia / horas * minutos * segundos 

#imprimir o ganho de massa por unidade de tempo, em miligramas por segundo 
print(f"O ganho de massa por unidade de tempo em miligramas por segundo é :, {ganho_de_massa_segundo} mg/s")