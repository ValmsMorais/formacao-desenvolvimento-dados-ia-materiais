def preco_valido(preco_centavos):
    return preco_centavos > 0

print(preco_valido(205))
print(preco_valido(0))
print(preco_valido(-10))
