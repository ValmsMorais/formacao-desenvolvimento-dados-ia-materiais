def calcular_total(preco_centavos, quantidade):
    return preco_centavos * quantidade

def formatar_dinheiro(valor_centavos):
    return f"R$ {valor_centavos // 100},{valor_centavos % 100:02d}"

print(formatar_dinheiro(calcular_total(1099, 2)))
