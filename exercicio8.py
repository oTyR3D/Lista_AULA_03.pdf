#A quantidade média de radiação solar que chega na superfície da Terra está em torno de 1 calcm-2 min-1. Expressar essa quantidade em unidades do Sistema Internacional, sabendo que 1
#caloria equivale a 4,18 J. R: 696,7 J m^-2 s^-1

quantidade_cal = 1  # Quantidade em cal/cm^2/min
calorie_to_joule = 4.18  # Conversão de calorias para joules
min_to_sec = 60  # Conversão de minutos para segundos
cm2_to_m2 = 0.0001  # Conversão de cm^2 para m^2

#calculo final 
quantidade_si = (quantidade_cal * calorie_to_joule) / (min_to_sec * cm2_to_m2) # 1 * 4.18 / 60 * 0.0001

#expresse a quantidade em unidades do sistema internacional (SI)
print("Quantidade em SI (J/m^2/s):", quantidade_si)
