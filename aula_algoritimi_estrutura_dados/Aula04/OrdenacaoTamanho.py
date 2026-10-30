"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1244 - Ordenação por Tamanho):
===============================================================================
O objetivo deste desafio é ordenar um conjunto de palavras (strings) de acordo 
com o seu comprimento/tamanho, em ordem DECRESCENTE (da maior palavra para a menor).

Regras de Ordenação:
1. As palavras devem ser ordenadas pelo seu tamanho (número de caracteres) em ordem 
   decrescente.
2. Caso duas ou mais palavras possuam o MESMO tamanho, a ordem relativa original 
   em que elas apareceram na entrada deve ser rigorosamente mantida (ordenação estável).
3. A primeira linha da entrada indica a quantidade N de casos de teste.
4. Para cada caso de teste, deve-se imprimir as palavras ordenadas separadas por 
   um único espaço em branco na mesma linha.

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
4
Top Coder comp Wedn at midnight
one three five
I love Cpp
sj a sa df r e w f d s a v c x z sd fd

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo 'N = 4'.
- Lendo linha 1: "Top Coder comp Wedn at midnight"
- Divisão em lista: palavras = ["Top", "Coder", "comp", "Wedn", "at", "midnight"]
- Tamanho de cada palavra:
  * "Top": 3
  * "Coder": 5
  * "comp": 4
  * "Wedn": 4
  * "at": 2
  * "midnight": 8

- Aplicação de 'palavras.sort(key=len, reverse=True)':
  Como o método .sort() do Python implementa o algoritmo Timsort (que é estável), 
  palavras de mesmo tamanho mantêm a ordem original de aparição ("comp" vem antes de "Wedn").
  
  * Tamanho 8: "midnight"
  * Tamanho 5: "Coder"
  * Tamanho 4: "comp", "Wedn" (mantém ordem)
  * Tamanho 3: "Top"
  * Tamanho 2: "at"

- Lista ordenada: ["midnight", "Coder", "comp", "Wedn", "Top", "at"]
- Saída formatada (" ".join(palavras)): "midnight Coder comp Wedn Top at"

-----------------------
[Caso de Teste 2]
- Lendo linha 2: "one three five"
- Divisão em lista: palavras = ["one", "three", "five"]
- Tamanho de cada palavra:
  * "one": 3
  * "three": 5
  * "five": 4
- Ordenação decrescente por tamanho:
  * Tamanho 5: "three"
  * Tamanho 4: "five"
  * Tamanho 3: "one"
- Lista ordenada: ["three", "five", "one"]
- Saída formatada: "three five one"

-----------------------
[Caso de Teste 3]
- Lendo linha 3: "I love Cpp"
- Divisão em lista: palavras = ["I", "love", "Cpp"]
- Tamanho de cada palavra:
  * "I": 1
  * "love": 4
  * "Cpp": 3
- Lista ordenada: ["love", "Cpp", "I"]
- Saída formatada: "love Cpp I"

-----------------------
[Caso de Teste 4]
- Lendo linha 4: "sj a sa df r e w f d s a v c x z sd fd"
- Divisão em lista: palavras = ["sj", "a", "sa", "df", "r", "e", "w", "f", "d", "s", "a", "v", "c", "x", "z", "sd", "fd"]
- Ordenação decrescente por tamanho mantendo estabilidade nos empates:
  * Tamanho 2: "sj", "sa", "df", "sd", "fd" (mantém sequência original)
  * Tamanho 1: "a", "r", "e", "w", "f", "d", "s", "a", "v", "c", "x", "z" (mantém sequência original)
- Saída formatada: "sj sa df sd fd a r e w f d s a v c x z"

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O programa executa um laço 'for i in range(N)' baseado na quantidade N de casos 
  de teste lida na primeira linha.
- O programa encerra automaticamente após processar exatamente os N casos de teste.
===============================================================================
"""

# Lê a quantidade total de casos de teste que serão processados
# Exemplo: input() -> "4", N = 4
N = int(input())

# Laço para iterar sobre cada caso de teste do problema
for i in range(N):

    # Lê a linha de entrada contendo a frase/conjunto de palavras e a divide nos espaços
    # O método .split() separa a string por espaços e retorna uma lista de palavras
    # Exemplo: input() -> "Top Coder comp Wedn at midnight"
    #          palavras -> ["Top", "Coder", "comp", "Wedn", "at", "midnight"]
    palavras = input().split()

    # Ordena a lista de palavras em ordem DECRESCENTE pelo comprimento (tamanho) de cada palavra
    # - key=len: especifica que a chave de comparação será o resultado da função len() (tamanho da string)
    # - reverse=True: ordena do maior para o menor
    # O algoritmo nativo do Python (Timsort) é ESTÁVEL, o que garante que palavras de mesmo tamanho
    # preservem exatamente a ordem de entrada original.
    # Exemplo: ["Top", "Coder", "comp", "Wedn", "at", "midnight"] -> ["midnight", "Coder", "comp", "Wedn", "Top", "at"]
    palavras.sort(key=len, reverse=True)

    # Junta todas as palavras da lista em uma única string separada por espaços e a imprime na tela
    # Exemplo: " ".join(["midnight", "Coder", ...]) -> "midnight Coder comp Wedn Top at"
    print(" ".join(palavras))