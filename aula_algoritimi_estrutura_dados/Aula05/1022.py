"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1022 - TDA Racional):
===============================================================================
O objetivo deste desafio é realizar operações aritméticas básicas (soma, subtração, 
multiplicação e divisão) entre dois números racionais (frazões N1/D1 e N2/D2) e 
apresentar o resultado na forma original e na forma simplificada.

Regras e Fórmulas de Cálculo:
1. Entrada: N1 / D1 <operador> N2 / D2
2. Operações:
   - Soma (+):          (N1*D2 + N2*D1) / (D1*D2)
   - Subtração (-):     (N1*D2 - N2*D1) / (D1*D2)
   - Multiplicação (*): (N1*N2) / (D1*D2)
   - Divisão (/):       (N1*D2) / (N2*D1)
3. Simplificação:
   - Para simplificar a fração resultante, calcula-se o Máximo Divisor Comum (MDC) 
     entre o valor absoluto do numerador e do denominador.
   - Ambos são divididos pelo MDC.
   - Se o denominador resultante for negativo, ajusta-se o sinal invertendo o sinal 
     de ambos para manter o formato padrão (denominador positivo).
4. Saída:
   - Exibir a fração resultante original seguida da fração simplificada:
     "N_orig/D_orig = N_simp/D_simp"

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
4
1 / 2 + 3 / 4
1 / 2 - 3 / 4
2 / 3 * 6 / 6
1 / 2 / 3 / 4

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo N = 4.
- Entrada: "1 / 2 + 3 / 4"
  * N1 = 1, D1 = 2, operador = '+', N2 = 3, D2 = 4
- Cálculo da Soma:
  * numerador   = 1 * 4 + 3 * 2 = 4 + 6 = 10
  * denominador = 2 * 4 = 8
- Guardando valores originais:
  * originalnumerador = 10, originaldenominador = 8
- Simplificação:
  * divisor = gcd(|10|, |8|) = gcd(10, 8) = 2
  * numerador   = 10 // 2 = 5
  * denominador = 8 // 2 = 4
  * denominador não é negativo, mantém os sinais.
- Saída gerada: "10/8 = 5/4"

-----------------------
[Caso de Teste 2]
- Entrada: "1 / 2 - 3 / 4"
  * N1 = 1, D1 = 2, operador = '-', N2 = 3, D2 = 4
- Cálculo da Subtração:
  * numerador   = 1 * 4 - 3 * 2 = 4 - 6 = -2
  * denominador = 2 * 4 = 8
- Guardando valores originais:
  * originalnumerador = -2, originaldenominador = 8
- Simplificação:
  * divisor = gcd(|-2|, |8|) = gcd(2, 8) = 2
  * numerador   = -2 // 2 = -1
  * denominador = 8 // 2 = 4
- Saída gerada: "-2/8 = -1/4"

-----------------------
[Caso de Teste 3]
- Entrada: "2 / 3 * 6 / 6"
  * N1 = 2, D1 = 3, operador = '*', N2 = 6, D2 = 6
- Cálculo da Multiplicação:
  * numerador   = 2 * 6 = 12
  * denominador = 3 * 6 = 18
- Guardando valores originais:
  * originalnumerador = 12, originaldenominador = 18
- Simplificação:
  * divisor = gcd(|12|, |18|) = gcd(12, 18) = 6
  * numerador   = 12 // 6 = 2
  * denominador = 18 // 6 = 3
- Saída gerada: "12/18 = 2/3"

-----------------------
[Caso de Teste 4]
- Entrada: "1 / 2 / 3 / 4"
  * N1 = 1, D1 = 2, operador = '/', N2 = 3, D2 = 4
- Cálculo da Divisão:
  * numerador   = 1 * 4 = 4
  * denominador = 2 * 3 = 6
- Guardando valores originais:
  * originalnumerador = 4, originaldenominador = 6
- Simplificação:
  * divisor = gcd(|4|, |6|) = gcd(4, 6) = 2
  * numerador   = 4 // 2 = 2
  * denominador = 6 // 2 = 3
- Saída gerada: "4/6 = 2/3"

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O programa executa um laço 'for _ in range(N)' baseado na quantidade N de casos 
  de teste lida na primeira linha.
- O programa encerra automaticamente após processar exatamente os N casos de teste.
===============================================================================
"""

# Importa a função gcd (Greatest Common Divisor / Máximo Divisor Comum) do módulo math
from math import gcd

# Lê a quantidade total de casos de teste que serão processados
# Exemplo: input() -> "4", N = 4
N = int(input())

# Laço para iterar sobre cada caso de teste do problema
for _ in range(N):
    # Lê a linha de entrada e desempacota cada componente da expressão matemática
    # A entrada "1 / 2 + 3 / 4" é separada por espaços, ignorando as barras estáticas das frações com '_'
    # Exemplo: N1 = '1', D1 = '2', operador = '+', N2 = '3', D2 = '4'
    N1, _, D1, operador, N2, _, D2 = input().split()

    # Converte os valores dos numeradores e denominadores de string para inteiro
    N1 = int(N1)
    D1 = int(D1)
    N2 = int(N2)
    D2 = int(D2)

    # Verifica qual operação deve ser realizada com base no caractere do operador
    if operador == '+':
        # Fórmula da Soma: (N1*D2 + N2*D1) / (D1*D2)
        numerador = N1 * D2 + N2 * D1
        denominador = D1 * D2
    elif operador == '-':
        # Fórmula da Subtração: (N1*D2 - N2*D1) / (D1*D2)
        numerador = N1 * D2 - N2 * D1
        denominador = D1 * D2
    elif operador == '*':
        # Fórmula da Multiplicação: (N1*N2) / (D1*D2)
        numerador = N1 * N2
        denominador = D1 * D2
    else:
        # Fórmula da Divisão: (N1*D2) / (D1*N2)
        numerador = N1 * D2
        denominador = D1 * N2

    # Armazena os valores originais da fração para serem exibidos antes da igualdade
    originalnumerador = numerador
    originaldenominador = denominador
    
    # Calcula o Máximo Divisor Comum (MDC) usando os valores absolutos do numerador e denominador
    # Exemplo: gcd(|10|, |8|) = gcd(10, 8) = 2
    divisor = gcd(
        abs(numerador),
        abs(denominador)
    )

    # Divide o numerador e o denominador pelo MDC para simplificar a fração (divisão inteira //)
    # Exemplo: 10 // 2 = 5, 8 // 2 = 4
    numerador //= divisor
    denominador //= divisor

    # Se o denominador for negativo após a simplificação, inverte os sinais do numerador e do denominador
    # Isso garante a convenção de ter o denominador sempre positivo
    if denominador < 0:
        numerador *= -1
        denominador *= -1

    # Imprime os resultados formatados no padrão: "fração_original = fração_simplificada"
    # Exemplo: "10/8 = 5/4"
    print(
        f"{originalnumerador}/{originaldenominador} = "
        f"{numerador}/{denominador}"
    )