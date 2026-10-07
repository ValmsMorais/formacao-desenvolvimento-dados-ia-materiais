produtos = [
    {"nome": "Caderno", "preco_centavos": 1250},
    {"nome": "Caneta", "preco_centavos": 205},
]
for produto in produtos:
    print(produto["nome"], produto["preco_centavos"])
print(produtos[1]["nome"])
