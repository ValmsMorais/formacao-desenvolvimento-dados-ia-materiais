def adicionar_nome(nomes, nome):
    nomes.append(nome)

catalogo = []
adicionar_nome(catalogo, "Caderno")
print(catalogo)

def trocar_lista(nomes):
    nomes = ["Outra lista"]

trocar_lista(catalogo)
print(catalogo)
