produto = "Caneta"
total_centavos = 205
reais = total_centavos // 100
centavos = total_centavos % 100
print(f"Produto: {produto}")
print(f"Total: R$ {reais},{centavos:02d}")
