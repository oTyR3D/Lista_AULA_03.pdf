#Rendimento agrícola norte-americano é expresso freqüentemente em bushels/acre. A quantas toneladas por hectare equivale um rendimento de soja de 40 bushels/acre? (1 acre = 4047 m2; 1
#bushel soja = 0,0272 ton). R: 2,69 ton/ha

rendimentos_bushels_acre = 40 

#conversoes usadas
acre_m2 = 4047 # 1 acre = 4047m2
bushel_tonelada = 0.0272 # 1 bushel de soja = 0,0272

#converter bushel por acre para bushel por metro quadrado m2
rendimentos_bushels_por_m2 = rendimentos_bushels_acre / acre_m2
# x = 40 / 4047 = 0,0098838645910

#converter bushels por metro quadrado para toneladas de hectares
rendimentos_toneladas_por_hectare = rendimentos_bushels_por_m2 * bushel_tonelada
# x = 0,0098838645910 * 0,0272 = 0,0002688411168(2,69)


#imprimir resultado
print("A quantidade de tonelas de soja de um rendimento de 40 bushels/acre por hectare é:", rendimentos_toneladas_por_hectare)
                                                                                                      #2,69