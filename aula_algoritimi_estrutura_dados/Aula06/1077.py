"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1077 - Infixa para Posfixa):
===============================================================================
O objetivo deste desafio é converter uma expressão matemática dada na forma 
infixa (operadores entre os operandos, como A + B) para a forma posfixa ou 
Notação Polonesa Reversa (operadores após os operandos, como AB+).

Regras da Conversão (Algoritmo Shunting-Yard):
1. A expressão pode conter operandos (letras e números), operadores binários 
   (+, -, *, /, ^) e parênteses '(' e ')'.
2. Ordem de Precedência/Prioridade dos Operadores:
   - Nível 3: Exponenciação (^) -> maior precedência.
   - Nível 2: Multiplicação (*) e Divisão (/) -> precedência intermediária.
   - Nível 1: Soma (+) e Subtração (-) -> menor precedência.
   - Nível 0: Parênteses '('.
3. Processamento caractere por caractere:
   - Operando (letra/número): vai direto para a saída.
   - Parêntese de abertura '(': é empilhado.
   - Parêntese de fechamento ')': desempilha os operadores para a saída até 
     encontrar o '(' correspondente, que é removido da pilha sem ir para a saída.
   - Operador: desempilha para a saída todos os operadores do topo da pilha 
     que possuam prioridade MAIOR OU IGUAL à do operador atual. Em seguida, 
     empilha o operador atual.
4. Após ler toda a expressão, desempilha todos os operadores restantes na pilha 
   para a saída.

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
3
A*2
(A*2+c-d)/2
(2*4/a^b)/(2*c)

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo N = 3
- Expressão: "A*2"
  * Caractere 'A' (operando):  saida = ['A'], pilha = []
  * Caractere '*' (operador):  prioridade('*') = 2. Pilha vazia -> pilha = ['*']
  * Caractere '2' (operando):  saida = ['A', '2'], pilha = ['*']
- Fim da string: desempilha a pilha -> desempilha '*' para a saída.
- Saída final: "A2*"

-----------------------
[Caso de Teste 2]
- Expressão: "(A*2+c-d)/2"
  * '(' -> empilha -> pilha = ['(']
  * 'A' -> operando -> saida = ['A']
  * '*' -> prioridade 2 -> pilha = ['(', '*']
  * '2' -> operando -> saida = ['A', '2']
  * '+' -> prioridade 1. Topo '*' tem prioridade 2 (2 >= 1) -> desempilha '*' -> saida = ['A', '2', '*']. Empilha '+' -> pilha = ['(', '+']
  * 'c' -> operando -> saida = ['A', '2', '*', 'c']
  * '-' -> prioridade 1. Topo '+' tem prioridade 1 (1 >= 1) -> desempilha '+' -> saida = ['A', '2', '*', 'c', '+']. Empilha '-' -> pilha = ['(', '-']
  * 'd' -> operando -> saida = ['A', '2', '*', 'c', '+', 'd']
  * ')' -> desempilha até '(' -> desempilha '-' -> saida = ['A', '2', '*', 'c', '+', 'd', '-']. Remove '(' -> pilha = []
  * '/' -> prioridade 2 -> pilha = ['/']
  * '2' -> operando -> saida = ['A', '2', '*', 'c', '+', 'd', '-', '2']
- Fim da string: desempilha '/' -> saida = ['A', '2', '*', 'c', '+', 'd', '-', '2', '/']
- Saída final: "A2*c+d-2/"

-----------------------
[Caso de Teste 3]
- Expressão: "(2*4/a^b)/(2*c)"
  * Processamento do primeiro parêntese "(2*4/a^b)":
    - '2', '*', '4' -> saida = ['2', '4'], pilha = ['(', '*']
    - '/' (prio 2) -> topo '*' (prio 2) desempilha -> saida = ['2', '4', '*'], pilha = ['(', '/']
    - 'a' -> saida = ['2', '4', '*', 'a']
    - '^' (prio 3) -> topo '/' (prio 2 < 3) -> empilha '^' -> pilha = ['(', '/', '^']
    - 'b' -> saida = ['2', '4', '*', 'a', 'b']
    - ')' -> desempilha '^' e '/' -> saida = ['2', '4', '*', 'a', 'b', '^', '/'], pilha = []
  * Operador '/' fora do parêntese: pilha = ['/']
  * Processamento do segundo parêntese "(2*c)":
    - '(' -> pilha = ['/', '(']
    - '2' -> saida = ['2', '4', '*', 'a', 'b', '^', '/', '2']
    - '*' -> pilha = ['/', '(', '*']
    - 'c' -> saida = ['2', '4', '*', 'a', 'b', '^', '/', '2', 'c']
    - ')' -> desempilha '*' -> saida = ['2', '4', '*', 'a', 'b', '^', '/', '2', 'c', '*'], pilha = ['/']
- Fim da string: desempilha '/' -> saida = ['2', '4', '*', 'a', 'b', '^', '/', '2', 'c', '*', '/']
- Saída final: "24*ab^/2c*/"

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O programa lê o número N de casos de teste na primeira linha.
- O laço 'for _ in range(N)' executa exatamente N vezes e encerra o programa naturalmente.
===============================================================================
"""

# Função que retorna o nível de precedência/prioridade de cada operador
def prioridade(operador):
    # Exponenciação possui a maior prioridade (nível 3)
    if operador == "^":
        return 3
    # Multiplicação e Divisão possuem prioridade intermediária (nível 2)
    if operador == "*" or operador == "/":
        return 2
    # Soma e Subtração possuem a menor prioridade de operadores (nível 1)
    if operador == "+" or operador == "-":
        return 1
    # Parênteses ou caracteres não-operadores possuem prioridade 0
    return 0

# Lê a quantidade total de casos de teste
# Exemplo: input() -> "3", N = 3
N = int(input())

# Laço para processar cada caso de teste individualmente
for _ in range(N):
    # Lê a expressão infixa e remove espaços das extremidades com .strip()
    # Exemplo: expressao = "A*2"
    expressao = input().strip()

    # Pilha para armazenar temporariamente os operadores e parênteses
    pilha = []
    # Lista para construir a expressão resultante na forma posfixa
    saida = []

    # Percorre cada caractere da expressão infixa
    for caractere in expressao:
        # Se o caractere for alfanumérico (letra ou número), vai diretamente para a saída
        # Exemplo: 'A'.isalnum() é True -> saida.append('A')
        if caractere.isalnum():
            saida.append(caractere)

        # Se for um parêntese de abertura '(', empilha para marcar o início de um bloco prioritário
        # Exemplo: pilha.append('(')
        elif caractere == "(":
            pilha.append(caractere)

        # Se for um parêntese de fechamento ')', desempilha tudo para a saída até encontrar o '('
        elif caractere == ")":
            # Enquanto a pilha não estiver vazia e o topo não for '(', desempilha para a saída
            while pilha and pilha[-1] != "(":
                saida.append(pilha.pop())
            # Remove o parêntese de abertura '(' da pilha sem adicioná-lo à saída
            if pilha:
                pilha.pop()
        else:
            # Caso seja um operador (+, -, *, /, ^):
            # Enquanto a pilha tiver elementos, o topo não for '(' e a prioridade do operador no topo
            # for MAIOR OU IGUAL à prioridade do operador atual, desempilha o topo para a saída
            # Exemplo: se topo é '*' (prio 2) e o atual é '+' (prio 1), desempilha '*'
            while (
                pilha
                and pilha[-1] != "("
                and prioridade(pilha[-1]) >= prioridade(caractere)
            ):
                saida.append(pilha.pop())
            # Empilha o operador atual após retirar os de maior/igual precedência
            pilha.append(caractere)

    # Após o término do laço da expressão, desempilha todos os operadores restantes na pilha para a saída
    while pilha:
        saida.append(pilha.pop())

    # Junta os caracteres da lista em uma única string e exibe a expressão posfixa final
    # Exemplo: "".join(['A', '2', '*']) -> "A2*"
    print("".join(saida))