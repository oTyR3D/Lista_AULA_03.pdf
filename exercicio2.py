#Uma unidade de área freqüentemente utilizada para expressar áreas de terra é o hectare, definido como 104 m2. Uma mina de carvão a céu aberto consome 75 hectares de terra, a uma profundidade
# de 26 m por ano. Calcule o volume de terra retirada neste tempo em km3. R: 0,0195 km3

area_hectares = 75 #75 hectares por terra da mina de carvão
profundida_metros = 26 #26 metro por ano

#Em primeiro lugar vamos converter todas as "medidas" na mesma unidade

# converter a area de hectares para metros quadrados 
area_metros_quadrados = area_hectares * 10000 # 1 hectare em metros quadrados
# x = 75 * 10000 = 750.000

#converter o volume de terra retirada para metros cubicos kcm3
volume_metro_cubicos = area_metros_quadrados * profundida_metros
# x = 750.000 * 26 = 19.500.000

# converter o volume para quilometros cubicos
volume_cubicos = volume_metro_cubicos / 1e9 # 1km3 = 1.000.000.000 m3
# x = 19.500.000

#Para calcularmos o volume vamos pensar num sólido geométrico, assim o volume (V) é dado por:

#V = Área da base x Altura

#V = 750.000m2 x 26m

#V = 19500000m3 = 0,0195 km3

#imprimir resultado
print("O volume da terra retirada neste tempo é :", volume_cubicos)
