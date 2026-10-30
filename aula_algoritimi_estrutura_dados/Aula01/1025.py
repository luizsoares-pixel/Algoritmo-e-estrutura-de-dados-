"""
OBJETIVO DO DESAFIO (Beecrowd 1025 - Onde estão os Mármores?):
Simular um jogo entre Raju e Meena. Raju tem N mármores com números que devem ser 
organizados em ordem crescente. Meena faz Q consultas perguntando em qual posição 
(baseada em 1) um determinado número aparece PELA PRIMEIRA VEZ. Se o número existir, 
o programa exibe sua primeira posição; caso contrário, informa que não foi encontrado. 
O processo se repete até que N e Q sejam ambos 0.

================================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO
================================================================================
Entrada de Exemplo:
4 1
2
3
5
1
5
5 2
1
3
3
3
1
2
3
0 0

--------------------------------------------------------------------------------
Passo a passo na memória:

--- CASO DE TESTE 1 (caso = 1) ---
1. '4 1':
   - N = 4 (lê 4 mármores)
   - Q = 1 (faz 1 consulta)

2. '2', '3', '5', '1' (N=4 números lidos):
   - marmores = [2, 3, 5, 1]

3. marmores.sort():
   - Lista ordenada: marmores = [1, 2, 3, 5]
   - Índices no Python (base 0):
     * Índice 0: 1
     * Índice 1: 2
     * Índice 2: 3
     * Índice 3: 5

4. '5' (Q=1 consulta lida):
   - Busca o número 5 usando bisect_left
   - bisect_left localiza o 5 no índice 3
   - Converte para posição baseada em 1: 3 + 1 = 4
   - Saída: "5 found at 4"

--- CASO DE TESTE 2 (caso = 2) ---
1. '5 2':
   - N = 5 (lê 5 mármores)
   - Q = 2 (faz 2 consultas)

2. '1', '3', '3', '3', '1' (N=5 números lidos):
   - marmores = [1, 3, 3, 3, 1]

3. marmores.sort():
   - Lista ordenada: marmores = [1, 1, 3, 3, 3]
   - Índices no Python (base 0):
     * Índice 0: 1
     * Índice 1: 1
     * Índice 2: 3 (1ª ocorrência do 3!)
     * Índice 3: 3
     * Índice 4: 3

4. '2' e '3' (Q=2 consultas lidas):
   - Consulta '2':
     * bisect_left indica índice 2, mas marmores[2] é 3 (diferente de 2)
     * Saída: "2 not found"
   - Consulta '3':
     * bisect_left acha a 1ª ocorrência do 3 no índice 2
     * Converte para posição baseada em 1: 2 + 1 = 3
     * Saída: "3 found at 3"

--- PARADA DO PROGRAMA ---
1. '0 0':
   - N = 0 e Q = 0 -> break encerra a execução.
================================================================================
"""
# Importa bisect_left para realizar busca binária eficiente (retorna a 1ª ocorrência)
from bisect import bisect_left

# Variável para controlar a numeração do caso de teste atual (CASE# 1, CASE# 2, etc.)
caso = 1

# Laço infinito para processar múltiplos casos de teste até a condição de parada
while True:
    # Lê N (quantidade de mármores) e Q (quantidade de consultas) na mesma linha
    N, Q = map(int, input().split())

    # Condição de parada: encerra o programa quando N e Q forem ambos iguais a 0
    if N == 0 and Q == 0:
        break

    # Lista vazia para armazenar os números dos mármores da rodada atual
    marmores = []

    # Repete N vezes para ler cada um dos mármores e adicioná-los à lista
    for _ in range(N):
        marmores.append(int(input()))

    # Ordena os mármores em ordem crescente (exigência do jogo e da busca binária)
    marmores.sort()

    # Imprime o cabeçalho do caso de teste atual
    print(f"CASE# {caso}:")

    # Repete Q vezes para processar cada consulta feita por Meena
    for _ in range(Q):
        # Lê o número a ser buscado na consulta atual
        numero = int(input())

        # Busca a menor posição onde o número está (ou deveria estar) via busca binária
        posicao = bisect_left(marmores, numero)

        # Verifica se a posição está no intervalo válido e se o número realmente existe lá
        if posicao < N and marmores[posicao] == numero:
            # Imprime informando a posição (somamos 1 pois os índices no Python começam em 0)
            print(f"{numero} found at {posicao+1}")
        else:
            # Imprime que o número não foi encontrado na coleção
            print(f"{numero} not found")

    # Incrementa o número do caso para o próximo teste
    caso += 1