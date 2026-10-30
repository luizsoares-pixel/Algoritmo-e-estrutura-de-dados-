"""
================================================================================
OBJETIVO DO DESAFIO:
--------------------------------------------------------------------------------
O problema solicita que seja determinado o menor número de trocas entre vagões
adjacentes necessárias para ordenar um trem de forma crescente (do vagão 1 até L).
Isso equivale a contar o número de inversões em uma permutação, o que é simular
o algoritmo Insertion Sort (ou Bubble Sort) contando a quantidade de trocas
efetuadas entre elementos vizinhos.

--------------------------------------------------------------------------------
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
--------------------------------------------------------------------------------
Entrada do Exemplo:
  3            -> Número de casos de teste (N = 3)
  3            -> Caso 1: Tamanho do trem (L = 3)
  1 3 2        -> Vagões iniciais
  4            -> Caso 2: Tamanho do trem (L = 4)
  4 3 2 1      -> Vagões iniciais
  2            -> Caso 3: Tamanho do trem (L = 2)
  2 1          -> Vagões iniciais

Rastreamento na Memória (Caso 1: TamanhoTrem = 3, vagoes = [1, 3, 2]):
  - Inicialização: trocas = 0

  - Loop principal:
    * i = 1: J = 1.
      Verifica vagoes[1] (3) < vagoes[0] (1)? Falso.
      Nenhuma troca. trocas = 0.

    * i = 2: J = 2.
      Verifica vagoes[2] (2) < vagoes[1] (3)? Verdadeiro!
      -> Troca vagoes[2] e vagoes[1]: vagoes passa a ser [1, 2, 3]
      -> trocas incrementado para 1
      -> J atualizado para 1

      Verifica vagoes[1] (2) < vagoes[0] (1)? Falso.
      Sai do laço while.

  Saída Gerada (Caso 1): "Optimal train swapping takes 1 swaps."

Rastreamento na Memória (Caso 2: TamanhoTrem = 4, vagoes = [4, 3, 2 1]):
  - Inicialização: trocas = 0
  - Loop de ordenação realiza trocas sucessivas entre elementos adjacentes:
    * Troca (4, 3) -> [3, 4, 2, 1], trocas = 1
    * Troca (4, 2) -> [3, 2, 4, 1], trocas = 2
    * Troca (3, 2) -> [2, 3, 4, 1], trocas = 3
    * Troca (4, 1) -> [2, 3, 1, 4], trocas = 4
    * Troca (3, 1) -> [2, 1, 3, 4], trocas = 5
    * Troca (2, 1) -> [1, 2, 3, 4], trocas = 6
  Saída Gerada (Caso 2): "Optimal train swapping takes 6 swaps."

Rastreamento na Memória (Caso 3: TamanhoTrem = 2, vagoes = [2, 1]):
  - Inicialização: trocas = 0
  - Loop de ordenação:
    * Troca (2, 1) -> [1, 2], trocas = 1
  Saída Gerada (Caso 3): "Optimal train swapping takes 1 swaps."

--------------------------------------------------------------------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
--------------------------------------------------------------------------------
O programa executa exatamente o número fixo de vezes determinado na leitura
inicial da variável 'casos' (for _ in range(casos)).
================================================================================
"""

# Lê a quantidade total de casos de teste a serem processados.
# Exemplo de entrada: "3" -> casos = 3
casos = int(input())

# O laço 'for' repete a lógica para cada caso de teste.
# Exemplo: executa o bloco 3 vezes para 3 casos de teste.
for _ in range(casos):

    # Lê o tamanho do trem (quantidade L de vagões no caso de teste atual).
    # Exemplo: "3" -> TamanhoTrem = 3
    TamanhoTrem = int(input())

    # Lê a sequência numérica que representa a ordem atual dos vagões e converte em lista.
    # Exemplo: "1 3 2" -> vagoes = [1, 3, 2]
    vagoes = list(map(int, input().split()))

    # Inicializa o contador de trocas necessárias para ordenar os vagões.
    # Exemplo: trocas = 0
    trocas = 0

    # Percorre a lista a partir do segundo elemento (índice 1) para aplicar o Insertion Sort.
    # Exemplo: para TamanhoTrem = 3, 'i' varia de 1 a 2.
    for i in range(1, TamanhoTrem):

        # Define a posição atual 'J' do elemento que tentaremos deslocar para a esquerda.
        # Exemplo: se i = 2, J inicia como 2.
        J = i

        # Laço que move o elemento da posição J para a esquerda enquanto ele for menor que o elemento anterior.
        # Exemplo: para vagoes = [1, 3, 2] e J = 2, testa se 2 < 3.
        while J > 0 and vagoes[J] < vagoes[J - 1]:

            # Troca o vagão atual com o vagão vizinho da esquerda.
            # Exemplo: vagoes[2], vagoes[1] = vagoes[1], vagoes[2] transforma [1, 3, 2] em [1, 2, 3].
            vagoes[J], vagoes[J - 1] = vagoes[J - 1], vagoes[J]

            # Incrementa o total de trocas em 1 para registrar a mudança realizada.
            # Exemplo: trocas passa de 0 para 1.
            trocas += 1

            # Decrementa 'J' para continuar checando o mesmo elemento na posição anterior.
            # Exemplo: J passa de 2 para 1.
            J -= 1

    # Imprime a frase formatada com a quantidade mínima de trocas calculada.
    # Exemplo de saída: "Optimal train swapping takes 1 swaps."
    print(f"Optimal train swapping takes {trocas} swaps.")