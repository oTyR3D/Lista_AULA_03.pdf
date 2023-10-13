#Uma estação meteorológica observou em determinado dia uma chuva de 18 mm. Quantos litros de água precipitaram durante esta chuva em cada hectare? R: 180 000 L/ha

chuva = 18

#converter milimetro para litros por metro quadrado (L/m²)
chuva_L_m2 = chuva # 1 milimetro de chuva para 1 litro por metro quadrado

#converter litros por metro quadrado (L/m²) litros por hectares (L/hec)
chuva_L_hec = chuva_L_m2 * 10000 # 1 hec por 10.000 L/m²

#imprimir a quantidade de litros de agua precipitada por hectare (L/hec)
print(f"A quantidade de agua precipitada por hectare é: {chuva_L_hec} L/hec.")