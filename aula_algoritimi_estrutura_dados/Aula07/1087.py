"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1087 - Dama):
===============================================================================
O objetivo deste desafio é calcular o menor número de movimentos necessários 
para uma Dama (Rainha) se mover de uma casa de origem (X1, Y1) para uma casa 
de destino (X2, Y2) em um tabuleiro de xadrez padrão de 8x8 casas.

Regras do Movimento da Dama:
1. A Dama pode se mover qualquer quantidade de casas na mesma linha, na mesma 
   coluna ou em qualquer uma das duas diagonais em um único movimento.
2. Casos Possíveis:
   - 0 movimentos: A casa de destino é exatamente a mesma casa de origem 
     (X1 == X2 e Y1 == Y2).
   - 1 movimento: A casa de destino está na mesma linha (X1 == X2), na mesma 
     coluna (Y1 == Y2) ou na mesma diagonal (|X1 - X2| == |Y1 - Y2|).
   - 2 movimentos: Qualquer outra posição do tabuleiro pode ser alcançada em no 
     máximo 2 movimentos (a Dama se move para a interseção de linha/coluna/diagonal 
     e depois para o destino).
3. Condição de parada: A entrada é encerrada quando X1 = Y1 = X2 = Y2 = 0.

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
4 4 6 2
3 5 3 5
5 5 4 3
0 0 0 0

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Coordenadas lidas: X1 = 4, Y1 = 4, X2 = 6, Y2 = 2
- Verificação das Condições:
  * Parada (0 0 0 0)? Falso.
  * Mesma posição (4 == 6 e 4 == 2)? Falso.
  * Mesma linha ou coluna (4 == 6 ou 4 == 2)? Falso.
  * Mesma diagonal?
    abs(4 - 6) = abs(-2) = 2
    abs(4 - 2) = abs(2) = 2
    Como 2 == 2, estão na mesma diagonal! Verdadeiro.
- Saída gerada para Caso 1: 1

-----------------------
[Caso de Teste 2]
- Coordenadas lidas: X1 = 3, Y1 = 5, X2 = 3, Y2 = 5
- Verificação das Condições:
  * Mesma posição (3 == 3 e 5 == 5)? Verdadeiro!
  * O número de movimentos necessários é 0.
- Saída gerada para Caso 2: 0

-----------------------
[Caso de Teste 3]
- Coordenadas lidas: X1 = 5, Y1 = 5, X2 = 4, Y2 = 3
- Verificação das Condições:
  * Mesma posição (5 == 4 e 5 == 3)? Falso.
  * Mesma linha ou coluna (5 == 4 ou 5 == 3)? Falso.
  * Mesma diagonal?
    abs(5 - 4) = 1
    abs(5 - 3) = 2
    Como 1 != 2, não estão na mesma diagonal. Falso.
  * Não caindo nos casos de 0 ou 1 movimento, o resultado é obrigatoriamente 2.
- Saída gerada para Caso 3: 2

-----------------------
[Caso de Teste 4]
- Coordenadas lidas: X1 = 0, Y1 = 0, X2 = 0, Y2 = 0
- Condição (X1 == 0 e Y1 == 0 e X2 == 0 e Y2 == 0) é Verdadeira.
- O laço é interrompido pelo comando 'break'.

===============================================================================
CONDIÇÃO DE PARADA DO PROGRAMA:
===============================================================================
- O programa roda em um laço 'while True'.
- A cada iteração, é lida uma linha contendo 4 inteiros.
- Quando todos os quatro valores lidos forem igual a zero ("0 0 0 0"), o comando 
  'break' é acionado e a execução do programa é finalizada.
===============================================================================
"""

# Laço infinito para processar múltiplos casos de teste de forma contínua
while True:
    # Lê os quatro inteiros da linha de entrada (coordenadas de origem e destino)
    # Exemplo: input() -> "4 4 6 2" -> X1 = 4, Y1 = 4, X2 = 6, Y2 = 2
    X1, Y1, X2, Y2 = map(int, input().split())

    # Verificação da condição de parada especificada no enunciado (quatro zeros)
    if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
        # Encerra o laço 'while True' e finaliza a execução do programa
        break

    # Caso 1: A casa de destino é a mesma casa onde a Dama já se encontra
    # Exemplo: (3, 5) para (3, 5) -> requer 0 movimentos
    if X1 == X2 and Y1 == Y2:
        print(0)
        
    # Caso 2a: A casa de destino está na mesma linha (X1 == X2) ou na mesma coluna (Y1 == Y2)
    # Exemplo: (4, 1) para (4, 8) -> requer 1 movimento na horizontal
    elif X1 == X2 or Y1 == Y2:
        print(1)
        
    # Caso 2b: A casa de destino está na mesma diagonal
    # A diferença absoluta entre as coordenadas X é igual à diferença absoluta entre as coordenadas Y
    # Exemplo: abs(4 - 6) == abs(4 - 2) -> 2 == 2 (verdadeiro) -> requer 1 movimento na diagonal
    elif abs(X1 - X2) == abs(Y1 - Y2):
        print(1)
        
    # Caso 3: Para qualquer outra posição no tabuleiro, a Dama precisará de no máximo 2 movimentos
    # Exemplo: (5, 5) para (4, 3) -> requer 2 movimentos
    else: 
        print(2)