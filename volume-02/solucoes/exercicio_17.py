def separar_dinheiro(valor_centavos):
    return valor_centavos // 100, valor_centavos % 100

reais, centavos = separar_dinheiro(1099)
print(reais)
print(centavos)
