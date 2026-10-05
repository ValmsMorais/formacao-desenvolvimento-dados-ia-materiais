nomes = ["Caderno", "Caneta"]
precos = [1250, 205]
for indice in range(len(nomes)):
    reais = precos[indice] // 100
    centavos = precos[indice] % 100
    print(f"{indice + 1} - {nomes[indice]}")
    print(f"Preço: R$ {reais},{centavos:02d}")
