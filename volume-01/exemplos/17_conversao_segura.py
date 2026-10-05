while True:
    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Digite um número inteiro")
        continue
    if quantidade <= 0:
        print("A quantidade deve ser positiva")
        continue
    break
print(f"Quantidade aceita: {quantidade}")
