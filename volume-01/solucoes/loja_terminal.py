nomes = []
precos = []
while True:
    comando = input("1 Cadastrar | 2 Pedir | 3 Sair: ").strip()
    if comando == "3":
        break
    if comando == "1":
        nome = input("Nome: ").strip()
        if nome == "":
            print("Informe um nome")
            continue
        try:
            preco = int(input("Preço em centavos: "))
        except ValueError:
            print("Digite um inteiro em centavos")
            continue
        if preco <= 0:
            print("O preço deve ser positivo")
            continue
        nomes.append(nome)
        precos.append(preco)
        print("Produto cadastrado")
    elif comando == "2":
        if len(nomes) == 0:
            print("Cadastre um produto primeiro")
            continue
        for indice in range(len(nomes)):
            print(f"{indice + 1} - {nomes[indice]}")
        try:
            opcao = int(input("Número do produto: "))
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Produto e quantidade devem ser inteiros")
            continue
        if opcao < 1 or opcao > len(nomes):
            print("Produto inexistente")
            continue
        if quantidade <= 0:
            print("Quantidade deve ser positiva")
            continue
        indice = opcao - 1
        total = precos[indice] * quantidade
        reais = total // 100
        centavos = total % 100
        print(f"Produto: {nomes[indice]}")
        print(f"Total: R$ {reais},{centavos:02d}")
    else:
        print("Escolha 1, 2 ou 3")
print("Loja encerrada")
