# Roteiro de testes — Loja com funções

Execute sua implementação no arquivo local `formacao-dados-ia/volume-02/projeto/loja_funcoes.py`. Reinicie antes de cada caso; o catálogo começa vazio. Respostas abaixo são enviadas ao terminal uma por vez. A referência completa está no arquivo local `formacao-dados-ia/volume-02/solucoes/loja_funcoes.py`.

| Caso | Respostas na ordem | Resultado esperado |
|---|---|---|
| Encerrar | 3 | Loja encerrada |
| Sem catálogo | 2; 3 | Cadastre um produto primeiro; menu; encerra |
| Pedido válido | 1; Caderno; 1250; 2; 1; 3; 3 | Total: R$ 37,50 |
| Outro produto | 1; Caneta; 205; 2; 1; 3; 3 | Total: R$ 6,15 |
| Nome vazio | 1; Enter vazio; 3 | Informe um nome; volta ao menu sem cadastrar |
| Nome só espaços | 1; três espaços; 3 | Informe um nome; sem cadastro |
| Preço textual | 1; Caderno; abc; 1250; 3 | Orienta inteiro e repete pergunta de preço; depois cadastra |
| Preço não positivo | 1; Caderno; 0; -1; 1250; 3 | Rejeita 0 e -1; repete pergunta; aceita 1250 |
| Quantidade inválida | 1; Caderno; 1250; 2; 1; abc; 0; 3; 3 | Rejeita abc e 0; repete quantidade; aceita 3; total R$ 37,50 |
| Produto fora da lista | 1; Caderno; 1250; 2; 9; 3 | Produto inexistente; não pergunta quantidade; volta ao menu |
| Opção de produto não positiva | 1; Caderno; 1250; 2; 0; 1; 2; 3 | Rejeita 0; repete produto; aceita 1; total R$ 25,00 |
| Dois produtos | 1; Caderno; 1250; 1; Caneta; 205; 2; 2; 3; 3 | Lista mostra dois produtos; total R$ 6,15 para Caneta |
| Menu desconhecido | 9; 3 | Escolha 1, 2 ou 3; menu; encerra |

Mensagens podem variar na implementação do aluno; aceitação, rejeição e totais precisam cumprir o enunciado. Não é necessário registrar progresso.
