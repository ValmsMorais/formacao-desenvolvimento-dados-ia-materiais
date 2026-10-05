quantidade = 3
preco_centavos = 1250
if quantidade <= 0:
    print("Quantidade inválida")
elif preco_centavos <= 0:
    print("Preço inválido")
else:
    print("Pedido pode ser calculado")
valido = quantidade > 0 and preco_centavos > 0
print(valido)
print(quantidade == 1 or quantidade == 3)
print(not valido)
