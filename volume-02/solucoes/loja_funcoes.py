def calcular_total(preco_centavos, quantidade):
    """Recebe inteiros positivos e devolve o total em centavos."""
    return preco_centavos * quantidade


def formatar_dinheiro(valor_centavos):
    """Recebe centavos inteiros não negativos e devolve texto em reais."""
    reais = valor_centavos // 100
    centavos = valor_centavos % 100
    return f"R$ {reais},{centavos:02d}"


def ler_inteiro_positivo(pergunta):
    """Repete a entrada até obter um inteiro positivo e o devolve."""
    while True:
        try:
            valor = int(input(pergunta))
        except ValueError:
            print("Digite um número inteiro")
            continue
        if valor <= 0:
            print("O valor deve ser maior que zero")
            continue
        return valor


def cadastrar_produto(produtos):
    """Valida a entrada e acrescenta um produto à lista recebida."""
    nome = input("Nome: ").strip()
    if nome == "":
        print("Informe um nome")
        return
    preco = ler_inteiro_positivo("Preço em centavos: ")
    produtos.append({"nome": nome, "preco_centavos": preco})
    print("Produto cadastrado")


def listar_produtos(produtos):
    """Mostra opções e preços sem modificar a lista recebida."""
    for numero, produto in enumerate(produtos, start=1):
        preco_formatado = formatar_dinheiro(produto["preco_centavos"])
        print(f"{numero} - {produto['nome']} - {preco_formatado}")


def fazer_pedido(produtos):
    """Recebe e confere um pedido e apresenta o total; não grava pedidos."""
    if len(produtos) == 0:
        print("Cadastre um produto primeiro")
        return
    listar_produtos(produtos)
    opcao = ler_inteiro_positivo("Número do produto: ")
    if opcao > len(produtos):
        print("Produto inexistente")
        return
    quantidade = ler_inteiro_positivo("Quantidade: ")
    produto = produtos[opcao - 1]
    total = calcular_total(produto["preco_centavos"], quantidade)
    print(f"Produto: {produto['nome']}")
    print(f"Total: {formatar_dinheiro(total)}")


def executar_loja():
    """Mantém o catálogo desta execução e controla o menu."""
    produtos = []
    while True:
        comando = input("1 Cadastrar | 2 Pedir | 3 Sair: ").strip()
        if comando == "3":
            break
        if comando == "1":
            cadastrar_produto(produtos)
        elif comando == "2":
            fazer_pedido(produtos)
        else:
            print("Escolha 1, 2 ou 3")
    print("Loja encerrada")


executar_loja()
