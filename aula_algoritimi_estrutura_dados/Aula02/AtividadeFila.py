"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1110 - Jogando Cartas Fora):
===============================================================================
O objetivo deste desafio é simular a manipulação de um baralho de cartas numeradas 
de 1 a N (com a carta 1 no topo e N na base) aplicando repetidamente uma sequência 
de duas operações até restar apenas uma única carta:

Operações Realizadas (enquanto houver 2 ou mais cartas):
1. Descartar a carta do topo.
2. Mover a próxima carta (a que ficou no topo) para a base do baralho.

Regras de Saída:
1. Para cada caso de teste, deve-se exibir a sequência de cartas descartadas, 
   separadas por vírgula e espaço: "Discarded cards: 1, 3, 5, ..."
2. Na linha seguinte, exibir a única carta restante: "Remaining card: X"
3. O programa deve processar múltiplos casos de teste até que N seja igual a 0 
   (condição de parada).

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
7
19
10
6
0

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo N = 7
- Inicializa a fila (deque) com cartas de 1 a 7:
  fila = deque([1, 2, 3, 4, 5, 6, 7])
- Inicializa descartadas = []

* Passagem 1 (len(fila) = 7):
  - Popleft (descarte): 1 -> descartadas = ["1"], fila = [2, 3, 4, 5, 6, 7]
  - Popleft e Append (vai para a base): 2 -> fila = [3, 4, 5, 6, 7, 2]

* Passagem 2 (len(fila) = 6):
  - Popleft (descarte): 3 -> descartadas = ["1", "3"], fila = [4, 5, 6, 7, 2]
  - Popleft e Append: 4 -> fila = [5, 6, 7, 2, 4]

* Passagem 3 (len(fila) = 5):
  - Popleft (descarte): 5 -> descartadas = ["1", "3", "5"], fila = [6, 7, 2, 4]
  - Popleft e Append: 6 -> fila = [7, 2, 4, 6]

* Passagem 4 (len(fila) = 4):
  - Popleft (descarte): 7 -> descartadas = ["1", "3", "5", "7"], fila = [2, 4, 6]
  - Popleft e Append: 2 -> fila = [4, 6, 2]

* Passagem 5 (len(fila) = 3):
  - Popleft (descarte): 4 -> descartadas = ["1", "3", "5", "7", "4"], fila = [6, 2]
  - Popleft e Append: 6 -> fila = [2, 6]

* Passagem 6 (len(fila) = 2):
  - Popleft (descarte): 2 -> descartadas = ["1", "3", "5", "7", "4", "2"], fila = [6]
  - Popleft e Append: 6 -> fila = [6]

* Término do laço interno: len(fila) = 1.

- Saída gerada para N = 7:
  Discarded cards: 1, 3, 5, 7, 4, 2
  Remaining card: 6

-----------------------
[Caso de Teste 2]
- Lendo N = 6
- fila = deque([1, 2, 3, 4, 5, 6])
- Passos de execução:
  * Descarta 1, move 2 -> fila = [3, 4, 5, 6, 2]
  * Descarta 3, move 4 -> fila = [5, 6, 2, 4]
  * Descarta 5, move 6 -> fila = [2, 4, 6]
  * Descarta 2, move 4 -> fila = [6, 4]
  * Descarta 6, move 4 -> fila = [4]
- Saída gerada para N = 6:
  Discarded cards: 1, 3, 5, 2, 6
  Remaining card: 4

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O programa executa um laço 'while True'.
- A cada iteração, lê o inteiro N.
- A condição 'if N == 0: break' encerra a execução do programa quando o valor 
  lido for zero (0).
===============================================================================
"""

# Importa a estrutura de dados 'deque' (double-ended queue) da biblioteca 'collections'
# O 'deque' permite inserções e remoções eficientes O(1) em ambas as extremidades (início e fim)
from collections import deque 

# Laço principal para processar múltiplos casos de teste até a entrada indicar 0
while True: 
    # Lê a quantidade de cartas do baralho para o caso de teste atual
    # Exemplo: input() -> "7", N = 7
    N = int(input())
    
    # Condição de parada: encerra o laço se o valor de N for igual a 0
    if N == 0:
        break
    
    # Cria uma fila (deque) com as cartas enumeradas de 1 até N
    # Exemplo para N = 7: fila = deque([1, 2, 3, 4, 5, 6, 7])
    fila = deque(range(1, N + 1))
    
    # Lista auxiliar para armazenar a sequência de cartas que forem descartadas
    descartadas = []
    
    # Repete o processo enquanto houver 2 ou mais cartas na fila
    while len(fila) > 1:
        # Operação 1: Remove a carta do topo (início da fila) com popleft(), converte para string e guarda no descarte
        # Exemplo: fila.popleft() -> 1; descartadas.append("1")
        descartadas.append(str(fila.popleft()))
        
        # Operação 2: Remove a nova carta do topo e a reinsere na base (final da fila) com append()
        # Exemplo: fila.popleft() -> 2; fila.append(2)
        fila.append(fila.popleft())
        
    # Imprime a lista de cartas descartadas formatada com vírgula e espaço entre os elementos
    # Exemplo: "Discarded cards: 1, 3, 5, 7, 4, 2"
    print("Discarded cards:", ", ".join(descartadas))
    
    # Imprime a única carta restante no baralho (posição 0 da fila)
    # Exemplo: "Remaining card: 6"
    print("Remaining card:", fila[0])