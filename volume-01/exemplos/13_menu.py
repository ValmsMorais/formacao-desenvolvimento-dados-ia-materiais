while True:
    comando = input("Digite continuar ou sair: ").strip().lower()
    if comando == "sair":
        break
    if comando != "continuar":
        print("Comando inválido")
        continue
    print("Executando uma atividade")
print("Programa encerrado")
