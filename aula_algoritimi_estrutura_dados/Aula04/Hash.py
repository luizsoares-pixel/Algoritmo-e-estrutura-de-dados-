"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1256 - Tabelas Hash):
===============================================================================
O objetivo deste desafio é simular o funcionamento de uma Tabela Hash (Tabela de 
Dispersão) com tratamento de colisões por encadeamento exterior (listas encadeadas).

Regras:
1. A primeira linha da entrada indica a quantidade N de casos de teste.
2. Cada caso de teste possui:
   - Uma linha com dois inteiros: M (quantidade de endereços-base/tamanho da tabela) 
     e C (quantidade de chaves a serem inseridas).
   - Uma linha com C números inteiros representando as chaves.
3. A função de dispersão (hash) utilizada é h(x) = x mod M, que calcula o índice 
   da tabela onde a chave 'x' deve ser inserida.
4. As chaves devem ser inseridas na ordem em que aparecem na entrada, mantendo a 
   sequência na lista de cada endereço-base.
5. Para a saída, cada endereço 'i' de 0 até M-1 deve ser impresso no formato:
   "i -> valor1 -> valor2 -> ... -> \"
   Se não houver elementos no endereço 'i', a saída deve ser apenas: "i -> \"
6. Entre dois casos de teste consecutivos, deve haver exatamente uma linha em branco.

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
2
13 9
44 45 49 70 27 73 92 97 95
7 8
35 12 2 17 19 51 88 86

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo 'casos = 2'.
- Lendo 'M = 13', 'C = 9'.
- Criando tabela vazia com 13 listas (índices 0 a 12):
  tabela = [[], [], [], [], [], [], [], [], [], [], [], [], []]
- Chaves lidas: [44, 45, 49, 70, 27, 73, 92, 97, 95]

- Inserções via h(x) = x % 13:
  * 44 % 13 = 5  -> tabela[5].append(44)   -> tabela[5] = [44]
  * 45 % 13 = 6  -> tabela[6].append(45)   -> tabela[6] = [45]
  * 49 % 13 = 10 -> tabela[10].append(49)  -> tabela[10] = [49]
  * 70 % 13 = 5  -> tabela[5].append(70)   -> tabela[5] = [44, 70]   (Colisão!)
  * 27 % 13 = 1  -> tabela[1].append(27)   -> tabela[1] = [27]
  * 73 % 13 = 8  -> tabela[8].append(73)   -> tabela[8] = [73]
  * 92 % 13 = 1  -> tabela[1].append(92)   -> tabela[1] = [27, 92]   (Colisão!)
  * 97 % 13 = 6  -> tabela[6].append(97)   -> tabela[6] = [45, 97]   (Colisão!)
  * 95 % 13 = 4  -> tabela[4].append(95)   -> tabela[4] = [95]

- Impressão do Caso de Teste 1:
  0 -> \
  1 -> 27 -> 92 -> \
  2 -> \
  3 -> \
  4 -> 95 -> \
  5 -> 44 -> 70 -> \
  6 -> 45 -> 97 -> \
  7 -> \
  8 -> 73 -> \
  9 -> \
  10 -> 49 -> \
  11 -> \
  12 -> \

- Como 'caso < casos - 1' (0 < 1), imprime uma linha em branco.

-----------------------
[Caso de Teste 2]
- Lendo 'M = 7', 'C = 8'.
- Criando tabela vazia com 7 listas (índices 0 a 6):
  tabela = [[], [], [], [], [], [], []]
- Chaves lidas: [35, 12, 2, 17, 19, 51, 88, 86]

- Inserções via h(x) = x % 7:
  * 35 % 7 = 0  -> tabela[0] = [35]
  * 12 % 7 = 5  -> tabela[5] = [12]
  * 2  % 7 = 2  -> tabela[2] = [2]
  * 17 % 7 = 3  -> tabela[3] = [17]
  * 19 % 7 = 5  -> tabela[5] = [12, 19]  (Colisão!)
  * 51 % 7 = 2  -> tabela[2] = [2, 51]   (Colisão!)
  * 88 % 7 = 4  -> tabela[4] = [88]
  * 86 % 7 = 2  -> tabela[2] = [2, 51, 86] (Colisão!)

- Impressão do Caso de Teste 2:
  0 -> 35 -> \
  1 -> \
  2 -> 2 -> 51 -> 86 -> \
  3 -> 17 -> \
  4 -> 88 -> \
  5 -> 12 -> 19 -> \
  6 -> \

- Como 'caso < casos - 1' é Falso (1 < 1 é Falso), não imprime linha em branco adicional.

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O número total de casos de teste é definido no início pela variável 'casos'.
- O laço 'for caso in range(casos)' executa exatamente o número estipulado de vezes 
  e o programa encerra naturalmente após o término do último caso.
===============================================================================
"""

# Lê o número total de casos de teste que serão processados
# Exemplo: input() -> "2", casos = 2
casos = int(input())

# Laço para processar cada caso de teste individualmente
for caso in range(casos):
    # Lê M (número de endereços/índices da tabela) e C (quantidade de chaves)
    # Exemplo: input() -> "13 9" -> M = 13, C = 9
    M, C = map(int, input().split())

    # Cria a estrutura da tabela Hash como uma lista de M sublistas vazias
    # Exemplo para M = 3: tabela = [[], [], []]
    tabela = [[] for _ in range(M)]

    # Lê todas as C chaves da linha seguinte e converte para uma lista de inteiros
    # Exemplo: input() -> "44 45 49 ..." -> valores = [44, 45, 49, ...]
    valores = list(map(int, input().split()))

    # Itera sobre cada chave recebida para inseri-la na tabela Hash
    for valor in valores:
        # Aplica a função de dispersão h(x) = x mod M para encontrar o índice do endereço
        # Exemplo: se valor = 44 e M = 13, posicao = 44 % 13 = 5
        posicao = valor % M

        # Adiciona o valor no final da lista encadeada correspondente ao índice calculado
        # Exemplo: tabela[5].append(44)
        tabela[posicao].append(valor)

    # Itera sobre todos os M endereços-base da tabela Hash para formatar a saída
    for i in range(M):
        # Imprime o índice do endereço seguido de " -> " sem quebrar a linha (end="")
        # Exemplo para i = 0: "0 -> "
        print(f"{i} -> ", end="")

        # Itera sobre todos os valores armazenados no endereço 'i'
        for valor in tabela[i]:
            # Imprime o valor seguido de " => " (atenção: no código fornecido imprime " valor => ", 
            # mas na formatação final resulta no encadeamento correto de elementos)
            # Exemplo: " 27 => " ou " 44 => "
            print(f"{valor} -> ", end="")

        # Imprime o caractere de barra invertida '\' indicando o fim da lista no endereço 'i' e quebra a linha
        # Exemplo: "\"
        print("\\")

    # Verifica se não é o último caso de teste para adicionar uma linha em branco entre os resultados
    # Exemplo: se caso = 0 e casos = 2, caso < 1 é Verdadeiro -> imprime linha em branco
    if caso < casos - 1:
        print()