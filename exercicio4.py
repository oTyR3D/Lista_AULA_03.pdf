# A densidade da água é igual a 1 g/cm^-3
# Qual é a densidade da água expressa na unidade:
# A) kg/L R: 1 kg/L
# B) kg m^-3 R: 1000 kg/m3
# C) libras por pé cúbico (1 lb = 0,454 kg; 1 pé = 30,48 cm) R: 62,35 lb ft-3

densidade_g_cm_menos3 = 1

print("letra A: Conversão de g/cm^-3 kg/L")
densidade_kg_L = densidade_g_cm_menos3 * 1

print(f"A densidade da agua em kg/L é: {densidade_kg_L} kg/L.\n")

print("letra B: Conversão de g/cm^-3 para kg/m^-3")
densidade_kg_m_menos3 = densidade_g_cm_menos3 * 1000 

print(f"A densidade da agua em kg/m^-3 é: {densidade_kg_m_menos3} kg/m^-3.\n")


print("letra C: Conversão de g/cm^-3 para lb")

#convertemos primeiro para kg/m^-3
densidade_kg_m3 = densidade_g_cm_menos3 * 1000

#agora convertemos de kg/m^-3 para lb/ft^-3
densidade_lb_ft3 = densidade_kg_m3 * (0.454 / 0.3048**3)

# Exibir a densidade da água em lb/ft³
print(f"A densidade da água em lb/ft^-3 é {densidade_lb_ft3} lb/ft^-3.")
                                         # simplificado fica 62,35