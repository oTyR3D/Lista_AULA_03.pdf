#Um cavalo-vapor(cv) equivale a 735,5 W. Qual é o consumo de energia de uma máquina de 5 cv que funciona durante 10 horas, em Joule e em eV? (1 eV = 1,6.10-19 J) R: 132.390.000J ou 8,2743.1026 eV

#primeiro iremos adcionar os dados da maquina e calcular os segundos de duração da maquina
energia_cv = 5 # maquina de 5 cv 
tp_cv = 10 #duração de funcionalidade da maquina 10 horas
tp_segundos = tp_cv * 36000 #conversão das horas de duração para os segundos de duração 

#converter de cv para W
energia_W = energia_cv * 735.5 

#calcular a energia em joule (J)
energia_J = energia_W * tp_segundos
# x = 735,5 * 36000 = 26,478,000

#converter joule para  elétron-volts (eV)
eV_J = 1.6e-19 # fator de conversão de (eV) para (J)
energia_eV = energia_J / eV_J

#imprimir o consumo de energia em joules (J) e em elétron-volts (eV)
print(f"O consumo de energia é de: {energia_J:.0f} J ou {energia_eV:.4e} eV.")
#calculo ira dar aproximadamente 1323900000 J e 8.2744e+27 eV 
#provavelmente o fator de conversao não esta completamente correto