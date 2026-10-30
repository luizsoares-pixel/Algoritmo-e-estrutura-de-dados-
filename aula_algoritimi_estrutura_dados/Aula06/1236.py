"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1236 - Compactação de Dados):
===============================================================================
O objetivo deste desafio é implementar um algoritmo de compactação simples para 
arquivos de texto que contêm longas sequências de zeros ('0') ou espaços em branco (' ').

Regras de Compactação:
1. Símbolos de Compactação:
   - Utiliza-se '$' para representar a compactação de sequências de espaços (' ').
   - Utiliza-se '#' para representar a compactação de sequências de zeros ('0').
2. Condição Mínima de Compactação:
   - Sequências de até 2 zeros ou 2 espaços NÃO devem ser compactadas (ex: "00" ou "  "), 
     pois a compactação ocuparia 2 caracteres e não traria ganho de espaço.
   - A compactação só ocorre para sequências de 3 ou mais caracteres repetidos.
3. Representação da Frequência:
   - A quantidade de repetições é gravada como o caractere da Tabela ASCII correspondente 
     à frequência (ex: para frequência 35, grava-se o caractere chr(35), isto é, '#').
4. Limite por Bloco (255 caracteres):
   - Se a sequência contiver mais de 255 repetições, ela deve ser dividida em múltiplos 
     blocos de no máximo 255 (ex: 380 zeros geram um bloco de 255 com "#" + chr(255) 
     e um bloco de 125 com "#" + chr(125)).
5. Outros caracteres (letras, números diferentes de zero, símbolos) são mantidos inalterados.

===============================================================================
EXEMPLO PRÁTICO RASTRESTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
3
1240000000000000000000000000000000002342340234Movimento
00                                  0TT
00f0a  s0                           00 5

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo N = 3
- Entrada: "1240000000000000000000000000000000002342340234Movimento"
- '1', '2', '4' -> não são '0' nem ' ' -> adiciona diretamente: resultado = ['1', '2', '4']
- Sequência de '0's detectada:
  * Contagem de zeros consecutivos: quantidade = 35
  * Como 35 >= 3 e 35 <= 255:
    - Adiciona o símbolo de compactação '#'
    - Adiciona o caractere ASCII correspondente a 35: chr(35) = '#'
    - resultado = ['1', '2', '4', '#', '#']
- '2', '3', '4', '2', '3', '4' -> adiciona diretamente
- '0' isolado (quantidade = 1 < 3) -> mantido como '0'
- '2', '3', '4', "Movimento" -> adiciona diretamente
- Saída formatada: "124##2342340234Movimento"

-----------------------
[Caso de Teste 2]
- Entrada: "00                                  0TT"
- Sequência '00' no início (quantidade = 2 < 3):
  * Não compacta -> adiciona "00" diretamente.
- Sequência de espaços ' ' (quantidade = 34):
  * Como 34 >= 3:
    - Adiciona o símbolo de compactação '$'
    - Adiciona o caractere ASCII correspondente a 34: chr(34) = '"' (ou '&' a depender da tabela)
    - resultado = ['0', '0', '$', '&']
- '0', 'T', 'T' -> mantidos normalmente.
- Saída formatada: "00$&0TT"

-----------------------
[Caso de Teste 3]
- Entrada: "00f0a  s0                           00 5"
- '00' (quantidade = 2) -> mantido "00"
- 'f', '0', 'a' -> mantidos
- '  ' (2 espaços) -> mantido "  "
- 's', '0' -> mantidos
- Sequência de 27 espaços -> compacta em '$' + chr(27)
- '00' -> mantido "00"
- ' ' (1 espaço) -> mantido ' '
- '5' -> mantido
- Saída formatada: "00f0a  s0$,00 5"

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O programa executa um laço 'for _ in range(N)' baseado no número N de casos 
  de teste lido na primeira linha.
- O programa encerra automaticamente após processar todas as N linhas.
===============================================================================
"""

# Lê a quantidade total de casos de teste que serão processados
# Exemplo: input() -> "3", N = 3
N = int(input())

# Laço para iterar sobre cada caso de teste
for _ in range(N):
    # Lê a linha de texto a ser compactada
    # Exemplo: texto = "1240000000000000000000000000000000002342340234Movimento"
    texto = input()

    # Lista para armazenar as partes da string compactada resultante
    resultado = []
    
    # Ponteiro/Índice para percorrer a string caractere a caractere
    i = 0

    # Percorre toda a extensão da string 'texto'
    while i < len(texto):
        # Verifica se o caractere atual é o caractere nulo '0'
        if texto[i] == '0':
            # Guarda a posição inicial da sequência de zeros
            inicio = i

            # Avança o ponteiro enquanto houver zeros consecutivos
            while i < len(texto) and texto[i] == '0':
                i += 1
            
            # Calcula a quantidade total de zeros encontrados na sequência
            # Exemplo: i = 38, inicio = 3 -> quantidade = 35
            quantidade = i - inicio

            # Só compacta se a quantidade de zeros for de pelo menos 3
            if quantidade >= 3:
                # Trata casos em que a sequência excede o limite de 255 caracteres por bloco
                while quantidade > 255:
                    # Adiciona o caractere especial de compactação de zeros '#'
                    resultado.append('#')
                    # Adiciona o caractere de valor ASCII 255 (bloco cheio)
                    resultado.append(chr(255))

                    # Subtrai 255 do total de repetições restantes
                    quantidade -= 255

                # Adiciona o símbolo de compactação '#' para o bloco final (ou único)
                resultado.append('#')
                # Adiciona o caractere ASCII correspondente ao número restante de repetições
                # Exemplo: chr(35) -> '#'
                resultado.append(chr(quantidade))

            else:
                # Caso a sequência tenha menos de 3 zeros (1 ou 2), não compacta e mantém os zeros originais
                # Exemplo: '0' * 2 -> "00"
                resultado.append('0' * quantidade)

        # Verifica se o caractere atual é um espaço em branco ' '
        elif texto[i] == ' ':
            # Guarda a posição inicial da sequência de espaços
            inicio = i

            # Avança o ponteiro enquanto houver espaços consecutivos
            while i < len(texto) and texto[i] == ' ':
                i += 1
            
            # Calcula a quantidade total de espaços encontrados na sequência
            # Exemplo: quantidade = 34
            quantidade = i - inicio

            # Só compacta se a quantidade de espaços for de pelo menos 3
            if quantidade >= 3:
                # Trata casos em que a sequência excede o limite de 255 caracteres por bloco
                while quantidade > 255:
                    # Adiciona o caractere especial de compactação de espaços '$'
                    resultado.append('$')
                    # Adiciona o caractere de valor ASCII 255 (bloco cheio)
                    resultado.append(chr(255))

                    # Subtrai 255 do total de repetições restantes
                    quantidade -= 255

                # Adiciona o símbolo de compactação '$' para o bloco final (ou único)
                resultado.append('$')
                # Adiciona o caractere ASCII correspondente ao número restante de repetições
                # Exemplo: chr(34) -> '"'
                resultado.append(chr(quantidade))

            else:
                # Caso a sequência tenha menos de 3 espaços (1 ou 2), não compacta e mantém os espaços originais
                # Exemplo: ' ' * 2 -> "  "
                resultado.append(' ' * quantidade)

        # Caso seja qualquer outro caractere (letras, números != '0', símbolos)
        else: 
            # Adiciona o caractere inalterado à lista de resultados
            # Exemplo: resultado.append('M')
            resultado.append(texto[i])
            
            # Avança o ponteiro para o próximo caractere
            i += 1

    # Junta todos os elementos compactados da lista em uma única string e exibe na tela
    # Exemplo: "".join(['1', '2', '4', '#', '#', ...])
    print(''.join(resultado))