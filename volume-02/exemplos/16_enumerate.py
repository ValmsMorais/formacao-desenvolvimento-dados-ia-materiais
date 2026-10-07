produtos = [
    {"nome": "Caderno", "preco_centavos": 1250},
    {"nome": "Caneta", "preco_centavos": 205},
]
for numero, produto in enumerate(produtos, start=1):
    print(f"{numero} - {produto['nome']}")
