def separar_dinheiro(valor_centavos):
    return valor_centavos // 100, valor_centavos % 100

partes = separar_dinheiro(3750)
print(partes)
reais, centavos = partes
print(reais)
print(centavos)
unico = (1,)
print(unico)
