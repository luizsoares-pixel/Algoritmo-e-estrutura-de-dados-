"""
===============================================================================
1. DOCSTRING INICIAL DO CÓDIGO
===============================================================================

- OBJETIVO DO DESAFIO:
  Simular o problema de eliminação circular (variante do problema de Josephus)
  com dois ponteiros/contadores simultâneos.
  1. N candidatos desempregados são dispostos em círculo numerados de 1 a N.
  2. Um oficial caminha no sentido horário contando 'k' candidatos ativos, 
     iniciando a busca a partir do candidato atual no sentido horário.
  3. Outro oficial caminha no sentido anti-horário contando 'm' candidatos ativos, 
     iniciando a busca a partir do candidato atual no sentido anti-horário.
  4. Ambos escolhem seus respectivos candidatos.
  5. Se os dois escolherem candidatos DIFERENTES, ambos são eliminados e 
     impressos no formato de par (ex: "  4  8").
  6. Se ambos escolherem a MESMA pessoa, apenas essa pessoa é eliminada e 
     impressa individualmente (ex: "  7").
  7. O processo se repete até que todos os N candidatos sejam removidos.
  8. Formatação de Saída: Cada número de pessoa deve ser formatado com campo
     de largura 3 alinhado à direita (ex: "%3d" em C / f"{num:3d}" em Python). 
     Pares ou elementos únicos eliminados na mesma rodada são separados por vírgula.

- EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
  * Entrada: N = 10, k = 4, m = 3
  
  * Rastreamento da Memória:
    - Pessoas em círculo: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    - Início: pos_k = 0 (Pessoa 1), pos_m = 9 (Pessoa 10)

    Rodada 1:
      - k=4 (sentido horário a partir de pos_k=0): 
        Conta 1 (Pessoa 1), 2 (Pessoa 2), 3 (Pessoa 3), 4 (Pessoa 4).
        Escolhe: Pessoa 4 (índice 3).
      - m=3 (sentido anti-horário a partir de pos_m=9): 
        Conta 1 (Pessoa 10), 2 (Pessoa 9), 3 (Pessoa 8).
        Escolhe: Pessoa 8 (índice 7).
      - Como 4 != 8: Ambos são removidos.
      - Saída parcial: "  4  8"
      - Pessoas restantes ativas: [1, 2, 3, 5, 6, 7, 9, 10]
      - Próximas posições de início: pos_k avança para índice 4 (Pessoa 5), 
        pos_m recua para índice 6 (Pessoa 7).

    Rodada 2:
      - k=4 (horário a partir da Pessoa 5): 
        Conta 1 (Pessoa 5), 2 (Pessoa 6), 3 (Pessoa 7), 4 (Pessoa 9 - pula 8 inativa).
        Escolhe: Pessoa 9 (índice 8).
      - m=3 (anti-horário a partir da Pessoa 7): 
        Conta 1 (Pessoa 7), 2 (Pessoa 6), 3 (Pessoa 5).
        Escolhe: Pessoa 5 (índice 4).
      - Como 9 != 5: Ambos são removidos.
      - Saída parcial: "  4  8,  9  5"
      - Pessoas restantes ativas: [1, 2, 3, 6, 7, 10]
      - Próximas posições de início: pos_k = índice 9 (Pessoa 10), pos_m = índice 3 (Pessoa 4 - inativa, recua p/ Pessoa 3).

    Rodada 3:
      - k=4 (horário a partir da Pessoa 10): 
        Conta 1 (Pessoa 10), 2 (Pessoa 1), 3 (Pessoa 2), 4 (Pessoa 3).
        Escolhe: Pessoa 3 (índice 2).
      - m=3 (anti-horário a partir da Pessoa 3): 
        Conta 1 (Pessoa 3), 2 (Pessoa 2), 3 (Pessoa 1).
        Escolhe: Pessoa 1 (índice 0).
      - Como 3 != 1: Ambos são removidos.
      - Saída parcial: "  4  8,  9  5,  3  1"
      - Pessoas restantes ativas: [2, 6, 7, 10]
      - Próximas posições de início: pos_k = índice 3 (Pessoa 4 - inativa -> vai p/ 6), pos_m = índice 9 (Pessoa 10).

    Rodada 4:
      - k=4 (horário a partir da Pessoa 6): 
        Conta 1 (Pessoa 6), 2 (Pessoa 7), 3 (Pessoa 10), 4 (Pessoa 2).
        Escolhe: Pessoa 2 (índice 1).
      - m=3 (anti-horário a partir da Pessoa 10): 
        Conta 1 (Pessoa 10), 2 (Pessoa 7), 3 (Pessoa 6).
        Escolhe: Pessoa 6 (índice 5).
      - Como 2 != 6: Ambos são removidos.
      - Saída parcial: "  4  8,  9  5,  3  1,  2  6"
      - Pessoas restantes ativas: [7, 10]
      - Próximas posições de início: pos_k = índice 2 (Pessoa 3 - inativa -> vai p/ 7), pos_m = índice 4 (Pessoa 5 - inativa -> vai p/ 10).

    Rodada 5:
      - k=4 (horário a partir da Pessoa 7): 
        Conta 1 (Pessoa 7), 2 (Pessoa 10), 3 (Pessoa 7), 4 (Pessoa 10).
        Escolhe: Pessoa 10 (índice 9).
      - m=3 (anti-horário a partir da Pessoa 10): 
        Conta 1 (Pessoa 10), 2 (Pessoa 7), 3 (Pessoa 10).
        Escolhe: Pessoa 10 (índice 9).
      - Como 10 == 10: Apenas a Pessoa 10 é removida.
      - Saída parcial: "  4  8,  9  5,  3  1,  2  6, 10"
      - Pessoas restantes ativas: [7]
      - Próximas posições de início: pos_k = índice 6 (Pessoa 7), pos_m = índice 6 (Pessoa 7).

    Rodada 6:
      - k=4 (horário a partir da Pessoa 7): 
        Apenas Pessoa 7 está ativa. Escolhe: Pessoa 7.
      - m=3 (anti-horário a partir da Pessoa 7): 
        Apenas Pessoa 7 está ativa. Escolhe: Pessoa 7.
      - Como 7 == 7: Apenas a Pessoa 7 é removida.
      - Saída final: "  4  8,  9  5,  3  1,  2  6, 10,  7"

  * CONDIÇÃO DE PARADA DO PROGRAMA:
    - O programa lê continuamente as entradas N, k, m.
    - A execução do loop principal é interrompida quando 'N == 0 and k == 0 and m == 0'.
===============================================================================
"""

import sys

# Loop principal para processar múltiplos casos de teste de entrada
while True:
    # Lê uma linha de entrada com os três inteiros N (total de pessoas), k (passo horário) e m (passo anti-horário)
    # Exemplo: input = "10 4 3" -> n = 10, k = 4, m = 3
    linha = sys.stdin.readline().split()
    
    # Verifica se a linha está vazia para evitar exceções ao final dos dados
    if not linha:
        break

    n, k, m = map(int, linha)

    # Condição de parada do programa: N=0, k=0 e m=0 sinalizam o fim dos testes
    # Exemplo: se entrada for "0 0 0", encerra a execução do programa
    if n == 0 and k == 0 and m == 0:
        break

    # Cria a lista com os identificadores das pessoas numeradas de 1 a N
    # Exemplo: n = 4 -> pessoas = [1, 2, 3, 4]
    pessoas = list(range(1, n + 1))

    # Cria uma lista booleana para rastrear se cada pessoa no círculo ainda está ativa/presente
    # Exemplo: n = 4 -> ativas = [True, True, True, True]
    ativas = [True] * n

    # Define o índice inicial do ponteiro k (sentido horário), começando da pessoa 1 (índice 0)
    pos_k = 0

    # Define o índice inicial do ponteiro m (sentido anti-horário), começando da pessoa N (índice n - 1)
    pos_m = n - 1

    # Contador para armazenar a quantidade total de pessoas já eliminadas do círculo
    quantidade_eliminados = 0

    # Lista que armazenará os blocos de texto formatados das escolhas de cada rodada
    resultado_rodadas = []

    # Processa as eliminações até que todas as N pessoas tenham sido removidas
    while quantidade_eliminados < n:
        
        # --- BUSCA DO CON TADOR HORÁRIO (k) ---
        # Inicializa a contagem restante de passos para o ponteiro k
        contador_k = k
        while contador_k > 0:
            # Se a pessoa no índice atual pos_k estiver ativa, decremente a contagem
            if ativas[pos_k]:
                contador_k -= 1
            # Se ainda faltam passos a contar, avança para a próxima posição no sentido horário (com rotação circular)
            if contador_k > 0:
                pos_k = (pos_k + 1) % n

        # Identifica o número da pessoa escolhida pelo contador k
        pessoa_k = pessoas[pos_k]

        # --- BUSCA DO CONTADOR ANTI-HORÁRIO (m) ---
        # Inicializa a contagem restante de passos para o ponteiro m
        contador_m = m
        while contador_m > 0:
            # Se a pessoa no índice atual pos_m estiver ativa, decremente a contagem
            if ativas[pos_m]:
                contador_m -= 1
            # Se ainda faltam passos a contar, recua para a posição anterior no sentido anti-horário (com rotação circular)
            if contador_m > 0:
                pos_m = (pos_m - 1) % n

        # Identifica o número da pessoa escolhida pelo contador m
        pessoa_m = pessoas[pos_m]

        # --- PROCESSAMENTO DA SELEÇÃO DA RODADA ---
        # Caso 1: Ambos os contadores escolheram a MESMA pessoa
        if pos_k == pos_m:
            # Formata a pessoa escolhida com largura de 3 caracteres alinhada à direita
            # Exemplo: pessoa_k = 7 -> "  7"
            resultado_rodadas.append(f"{pessoa_k:3d}")

            # Marca a pessoa como eliminada
            ativas[pos_k] = False

            # Incrementa em 1 a quantidade de pessoas removidas
            quantidade_eliminados += 1
        
        # Caso 2: Os contadores escolheram pessoas DIFERENTES
        else:
            # Formata ambas as pessoas escolhidas com largura de 3 caracteres cada
            # Exemplo: pessoa_k = 4, pessoa_m = 8 -> "  4  8"
            resultado_rodadas.append(f"{pessoa_k:3d}{pessoa_m:3d}")

            # Marca ambas as pessoas como eliminadas
            ativas[pos_k] = False
            ativas[pos_m] = False

            # Incrementa em 2 a quantidade de pessoas removidas
            quantidade_eliminados += 2

    # Imprime todas as eliminações formatadas, separadas por vírgula
    # Exemplo: "  4  8,  9  5,  3  1,  2  6, 10,  7"
    print(",".join(resultado_rodadas))