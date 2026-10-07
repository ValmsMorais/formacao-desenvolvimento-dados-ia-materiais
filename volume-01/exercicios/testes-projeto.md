# Roteiro de testes do projeto

Execute o arquivo local `formacao-dados-ia/volume-01/projeto/loja_terminal.py`. Compare cada entrada com o comportamento esperado. Não é necessário registrar progresso.

- 01 | pedir antes de cadastrar | orienta cadastrar primeiro
- 02 | cadastrar nome vazio | rejeita nome
- 03 | cadastrar Caderno e abc | orienta inteiro sem cadastrar
- 04 | cadastrar Caderno e 0 | rejeita preço
- 05 | cadastrar Caderno e 1250 | confirma cadastro
- 06 | pedir opção 1 e quantidade 3 | R$ 37,50
- 07 | pedir opção 9 e quantidade 1 | produto inexistente
- 08 | pedir opção 1 e quantidade 0 | quantidade deve ser positiva
- 09 | pedir opção abc | orienta inteiros e retorna ao menu
- 10 | cadastrar Caneta e 205 depois pedir 2 e 3 | R$ 6,15
- 11 | comando 9 | orienta escolher 1 2 ou 3
- 12 | comando 3 | Loja encerrada
- 13 | reiniciar e pedir | catálogo vazio e orientação para cadastrar
