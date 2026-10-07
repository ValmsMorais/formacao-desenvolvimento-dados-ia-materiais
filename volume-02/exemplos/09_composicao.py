def calcular_total(preco_centavos, quantidade):
    return preco_centavos * quantidade

def formatar_dinheiro(valor_centavos):
    reais = valor_centavos // 100
    centavos = valor_centavos % 100
    return f"R$ {reais},{centavos:02d}"

total = calcular_total(205, 3)
print(formatar_dinheiro(total))
