produtos = [
    {"nome": "Caderno"},
    {"nome": "Caneta"},
    {"nome": "Borracha"},
]
for numero, produto in enumerate(produtos, start=1):
    print(f"{numero} - {produto['nome']}")
