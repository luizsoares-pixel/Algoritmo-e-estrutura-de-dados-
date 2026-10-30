"""
OBJETIVO DO DESAFIO (Beecrowd 1068 - Balanço de Parênteses I):
Verificar se os parênteses em expressões matemáticas estão balanceados e corretos[cite: 2].
Para que a expressão seja considerada correta ("correct")[cite: 2]:
1. Todo parêntese a fechar ')' deve ter um parêntese a abrir '(' correspondente antes dele[cite: 2].
2. Não pode haver parênteses a fechar ')' sem um parêntese a abrir '(' prévio[cite: 2].
3. O número total de parênteses a abrir '(' e a fechar ')' deve ser exatamente igual[cite: 2].
Caso contrário, a saída deve ser "incorrect"[cite: 2].
A leitura deve continuar até ao fim do arquivo (EOF - End Of File)[cite: 2].

================================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO
================================================================================
Entrada de Exemplo:
a+(b*c)-2-a
(a+b*(2-c)-2+a)*2
(a*b-(2+c)
2*(3-a))
)3+b*(2-c)(

--------------------------------------------------------------------------------
Passo a passo na memória:

--- EXPRESSÃO 1: "a+(b*c)-2-a" ---
1. Caractere '(': adiciona à pilha -> pilha = ['(']
2. Caractere ')': remove da pilha (há um '(' correspondente) -> pilha = []
3. Fim da string: correta = True e pilha vazia len(pilha) == 0.
   - Saída: "correct"

--- EXPRESSÃO 2: "(a+b*(2-c)-2+a)*2" ---
1. Primeiro '(': pilha = ['(']
2. Segundo '(': pilha = ['(', '(']
3. Primeiro ')': pop() da pilha -> pilha = ['(']
4. Segundo ')': pop() da pilha -> pilha = []
5. Fim da string: correta = True e pilha vazia.
   - Saída: "correct"

--- EXPRESSÃO 3: "(a*b-(2+c)" ---
1. Primeiro '(': pilha = ['(']
2. Segundo '(': pilha = ['(', '(']
3. Primeiro ')': pop() da pilha -> pilha = ['(']
4. Fim da string: sobrou '(' na pilha -> len(pilha) != 0 (expressão incompleta).
   - Saída: "incorrect"

--- EXPRESSÃO 4: "2*(3-a))" ---
1. Primeiro '(': pilha = ['(']
2. Primeiro ')': pop() da pilha -> pilha = []
3. Segundo ')': tenta fazer pop(), mas a pilha está vazia (len(pilha) == 0)!
   - Marca correta = False e interrompe o loop (break).
   - Saída: "incorrect"

--- EXPRESSÃO 5: ")3+b*(2-c)(" ---
1. Primeiro ')': tenta processar, mas a pilha está vazia (len(pilha) == 0)!
   - Marca correta = False e interrompe o loop (break).
   - Saída: "incorrect"
================================================================================
"""

# Laço contínuo para processar todas as linhas até o final da entrada (EOF)
while True:
    try:
        # Lê uma linha contendo a expressão matemática
        # Exemplo: "a+(b*c)-2-a"
        expressao = input()

        # Pilha (lista) para guardar os parênteses de abertura '(' encontrados
        pilha = []
        
        # Flag/booleano para indicar se a expressão permanece válida durante a leitura
        correta = True

        # Percorre a string caractere por caractere
        for caractere in expressao:

            # Se encontrar um parêntese a abrir, empilha-o
            if caractere == '(':
                pilha.append(caractere)

            # Se encontrar um parêntese a fechar, tenta desempilhar
            elif caractere == ')':

                # Se a pilha estiver vazia, significa que há um ')' sem o seu '(' prévio
                if len(pilha) == 0:
                    correta = False
                    break  # Encerra a verificação da linha atual antecipadamente

                # Remove o '(' correspondente do topo da pilha
                pilha.pop()

        # A expressão é válida apenas se a flag 'correta' for True E se todos os
        # parênteses abertos tiverem sido fechados (pilha completamente vazia no final)
        if correta and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")

    # Captura a exceção de fim de arquivo (EOF) para encerrar a execução do programa
    except EOFError:
        break