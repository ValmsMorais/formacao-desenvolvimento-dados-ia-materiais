produto = {"nome": "Caderno", "preco_centavos": 1250}
print("estoque" in produto)
print(produto.get("estoque"))
print(produto.get("estoque", 0))
for chave, valor in produto.items():
    print(chave, valor)
