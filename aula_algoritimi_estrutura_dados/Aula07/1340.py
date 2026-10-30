"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1340 - Eu Posso Adivinhar a Estrutura de Dados!):
===============================================================================
O objetivo deste desafio é identificar qual estrutura de dados está sendo utilizada 
com base em uma sequência de operações de inserção (comando 1) e remoção (comando 2).

As três estruturas avaliadas são:
1. Pilha / Stack (LIFO - Last In, First Out): O último elemento inserido é o primeiro a sair.
2. Fila / Queue (FIFO - First In, First Out): O primeiro elemento inserido é o primeiro a sair.
3. Fila de Prioridade / Priority Queue: O maior elemento inserido é sempre o primeiro a sair.

Regras de Classificação:
- 'stack': Apenas o comportamento de pilha é válido.
- 'queue': Apenas o comportamento de fila é válido.
- 'priority queue': Apenas o comportamento de fila de prioridade é válido.
- 'impossible': Nenhuma das três estruturas é capaz de reproduzir as saídas obtidas.
- 'not sure': Mais de uma estrutura é válida para a sequência de operações dada.

Condição de Parada:
- A entrada contém múltiplos casos de teste e é finalizada por Fim de Arquivo (EOF).

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
6
1 1
1 2
1 3
2 1
2 2
2 3

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo N = 6
- Inicialização:
  * pilha = [], fila = deque(), prioridade = []
  * epilha = True, efila = True, eprioridade = True

* Op 1 1: Insere 1 -> pilha = [1], fila = [1], prioridade = [-1]
* Op 1 2: Insere 2 -> pilha = [1, 2], fila = [1, 2], prioridade = [-2, -1]
* Op 1 3: Insere 3 -> pilha = [1, 2, 3], fila = [1, 2, 3], prioridade = [-3, -1, -2]

* Op 2 1: Remove elemento e espera '1'
  - Pilha remove topo (3): 3 != 1 -> epilha = False
  - Fila remove início (1): 1 == 1 -> efila = True
  - Prioridade remove maior (3): 3 != 1 -> eprioridade = False

* Op 2 2: Remove elemento e espera '2'
  - Fila remove início (2): 2 == 2 -> efila = True

* Op 2 3: Remove elemento e espera '3'
  - Fila remove início (3): 3 == 3 -> efila = True

- Avaliação das Possibilidades:
  epilha = False, efila = True, eprioridade = False
  possibilidades = sum([False, True, False]) = 1
- Saída gerada: "queue"

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O laço 'while True' tenta ler o valor 'N' (quantidade de operações) a cada caso de teste.
- Quando o arquivo de entrada termina, o 'input()' dispara uma exceção 'EOFError', 
  que é capturada pelo bloco 'except EOFError', acionando o 'break' para encerrar o programa.
===============================================================================
"""

# Importa deque para implementar uma fila eficiente (FIFO)
from collections import deque
# Importa heapq para implementar a fila de prioridade usando uma max-heap
import heapq 

# Laço principal para processar múltiplos casos de teste até o Fim de Arquivo (EOF)
while True:
    try:
        # Lê a quantidade de operações do caso de teste atual
        # Exemplo: input() -> "6", N = 6
        N = int(input())
    except EOFError:
        # Interrompe o laço e finaliza o programa ao atingir o final da entrada
        break

    # Estruturas de dados para simular as 3 possibilidades simultaneamente
    pilha = []
    fila = deque()
    prioridade = []

    # Flags booleanas para acompanhar se cada estrutura continua sendo válida
    epilha = True
    efila = True
    eprioridade = True

    # Processa cada uma das N operações do caso de teste
    for _ in range(N):
        # Lê o tipo de operação (1 = inserir, 2 = remover) e o valor correspondente
        # Exemplo: input() -> "1 2" -> operacao = 1, valor = 2
        operacao, valor = map(int, input().split())

        # Operação 1: Inserção de um elemento nas três estruturas
        if operacao == 1:
            pilha.append(valor)             # Empilha no topo da pilha
            fila.append(valor)              # Enfileira no final da fila
            heapq.heappush(prioridade, -valor) # Inserção na heap (sinal negativo para simular Maior Primeiro)

        # Operação 2: Remoção e verificação se o valor removido bate com o esperado
        else:
            # --- Teste da Pilha (LIFO) ---
            if not pilha:
                epilha = False
            else:
                removido = pilha.pop() # Remove do topo da pilha
                if removido != valor:
                    epilha = False

            # --- Teste da Fila (FIFO) ---
            if not fila:
                efila = False
            else:
                removido = fila.popleft() # Correção: remove do INÍCIO da fila (popleft)
                if removido != valor:
                    efila = False

            # --- Teste da Fila de Prioridade (Maior valor) ---
            if not prioridade:
                eprioridade = False
            else:
                removido = -heapq.heappop(prioridade) # Desfaz a negação para obter o maior valor
                if removido != valor:
                    eprioridade = False

    # Soma a quantidade de estruturas que continuam sendo válidas (True = 1, False = 0)
    possibilidades = sum([epilha, efila, eprioridade])

    # Correção: As verificações da resposta final foram movidas para FORA do laço de leitura das operações
    if possibilidades == 0:
        print("impossible")
    elif possibilidades > 1:
        print("not sure")
    elif epilha:
        print("stack")
    elif efila:
        print("queue")
    else:
        print("priority queue")