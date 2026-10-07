# Testes do projeto

Execute sua implementação no arquivo local `formacao-dados-ia/volume-01/projeto/loja_terminal.py`. O código de referência fica no arquivo local `formacao-dados-ia/volume-01/solucoes/loja_terminal.py`. Cada sequência abaixo informa respostas no terminal, uma por vez. Reinicie o programa antes de cada caso. Os dados não são preservados ao encerrar.

| Caso | Entradas na ordem | Resultado esperado |
|---|---|---|
| Pedido sem catálogo | 2; 3 | Cadastre um produto primeiro; Loja encerrada |
| Nome vazio | 1; Enter sem texto; 3 | Informe um nome; menu reaparece; Loja encerrada |
| Preço textual | 1; Caderno; abc; 3 | Digite um inteiro em centavos; não cadastra; Loja encerrada |
| Preço zero | 1; Caderno; 0; 3 | O preço deve ser positivo; não cadastra |
| Pedido válido | 1; Caderno; 1250; 2; 1; 3; 3 | Produto cadastrado; Produto: Caderno; Total: R$ 37,50; Loja encerrada |
| Quantidade zero | 1; Caderno; 1250; 2; 1; 0; 3 | Quantidade deve ser positiva; não calcula; menu reaparece |
| Produto inexistente | 1; Caderno; 1250; 2; 9; 1; 3 | Produto inexistente; não calcula; menu reaparece |
| Opção textual | 1; Caderno; 1250; 2; abc; 3 | Produto e quantidade devem ser inteiros; retorna ao menu antes de perguntar quantidade |
| Centavos com zero | 1; Caneta; 205; 2; 1; 3; 3 | Total: R$ 6,15 |
| Comando desconhecido | 9; 3 | Escolha 1, 2 ou 3; Loja encerrada |

Textos de perguntas e orientações podem variar na implementação do aluno; a aceitação, rejeição e os totais devem corresponder aos casos.
