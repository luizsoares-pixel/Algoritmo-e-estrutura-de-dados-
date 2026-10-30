"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1259 / 1055 / Dicionário de Frequência de Caracteres):
===============================================================================
O desafio consiste em ler linhas de texto (com até 1000 caracteres) e contar a 
frequência de cada caractere presente na linha, convertendo-os para seus respectivos 
valores numéricos na tabela ASCII.

Regras de Ordenação da Saída:
1. Imprimir em ordem ASCENDENTE (crescente) de frequência.
2. Se dois ou mais caracteres tiverem a MESMA frequência, o critério de desempate 
   é a ordem DECRESCENTE (do maior para o menor) do código ASCII.
3. Imprimir cada linha no formato: "<Código ASCII> <Frequência>".
4. Imprimir uma linha em branco separando os conjuntos de saída de dois casos de teste.
5. A leitura da entrada é finalizada ao atingir o Fim de Arquivo (EOF) ou através do 
   número de casos especificado.

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
2
AAABBC
122333

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo 'N = 2'.
- Lendo 'texto = "AAABBC"'.
- Mapeamento para ASCII e Frequência:
  * 'A' -> ord('A') = 65 -> frequencia[65] = 3
  * 'B' -> ord('B') = 66 -> frequencia[66] = 2
  * 'C' -> ord('C') = 67 -> frequencia[67] = 1
- Dicionário gerado: frequencia = {65: 3, 66: 2, 67: 1}
- Chaves obtidas: caracteres = [65, 66, 67]

- Ordenação com key = lambda codigo: (frequencia[codigo], -codigo):
  * Para 65: tupla da chave = (3, -65)
  * Para 66: tupla da chave = (2, -66)
  * Para 67: tupla da chave = (1, -67)
  * Lista após ordenar por menor frequência (e maior ASCII em empate):
    caracteres = [67, 66, 65]

- Saída gerada para Caso 1:
  67 1
  66 2
  65 3

- Como 'caso < N - 1' (0 < 1), imprime uma linha em branco.

-----------------------
[Caso de Teste 2]
- Lendo 'texto = "122333"'.
- Mapeamento para ASCII e Frequência:
  * '1' -> ord('1') = 49 -> frequencia[49] = 1
  * '2' -> ord('2') = 50 -> frequencia[50] = 2
  * '3' -> ord('3') = 51 -> frequencia[51] = 3
- Dicionário gerado: frequencia = {49: 1, 50: 2, 51: 3}
- Chaves obtidas: caracteres = [49, 50, 51]

- Ordenação com key = lambda codigo: (frequencia[codigo], -codigo):
  * Para 49: tupla da chave = (1, -49)
  * Para 50: tupla da chave = (2, -50)
  * Para 51: tupla da chave = (3, -51)
  * Lista ordenada: caracteres = [49, 50, 51]

- Saída gerada para Caso 2:
  49 1
  50 2
  51 3

- Como 'caso < N - 1' é Falso (1 < 1 é Falso), não imprime linha em branco final.

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O programa executa um laço 'for caso in range(N)' baseado na variável N lida no início.
- Nota: Para questões onde a entrada é por EOF (sem um N fixo na primeira linha), o código 
  pode ser adaptado com 'while True' e 'try/except EOFError'. No código fornecido, o laço 
  encerra automaticamente após processar exatamente N casos de teste.
===============================================================================
"""

# Lê a quantidade total de casos de teste que serão processados
# Exemplo: input() -> "2", N = 2
N = int(input())

# Laço para iterar sobre cada caso de teste
for caso in range(N):
    # Lê a linha de texto enviada no caso de teste atual
    # Exemplo: input() -> "AAABBC"
    texto = input()
    
    # Dicionário para armazenar a contagem de frequência indexada pelo código ASCII do caractere
    # Exemplo de chave/valor: {65: 3, 66: 2}
    frequencia = {}

    # Itera sobre cada caractere contido na linha de texto lida
    for caractere in texto:
        # Obtém o valor numérico inteiro correspondente ao caractere na tabela ASCII
        # Exemplo: ord('A') -> 65
        codigo = ord(caractere)

        # Se o código ASCII ainda não estiver no dicionário, inicializa sua contagem em 0
        if codigo not in frequencia:
            frequencia[codigo] = 0

        # Incrementa em 1 a contagem de frequência do código ASCII correspondente
        frequencia[codigo] += 1

    # Extrai uma lista contendo apenas os códigos ASCII únicos presentes no dicionário
    # Exemplo: [65, 66, 67]
    caracteres = list(frequencia.keys())

    # Ordena os códigos ASCII usando dois critérios combinados (tupla):
    # 1º critério: frequencia[codigo] em ordem crescente (menor frequência primeiro)
    # 2º critério: -codigo em ordem crescente (o sinal negativo inverte o valor de forma que o maior ASCII fique na frente em caso de empate)
    # Exemplo: (frequencia[67], -67) -> (1, -67), garantindo que frequência 1 venha antes de 2, e ASCII 67 venha antes de 66 se tivessem a mesma frequência.
    caracteres.sort(
        key=lambda codigo: (frequencia[codigo], -codigo)
    )

    # Itera sobre a lista de caracteres já devidamente ordenada
    for codigo in caracteres:
        # Imprime o código ASCII e sua frequência separados por um espaço
        # Exemplo: 67 1
        print(codigo, frequencia[codigo])

    # Verifica se não é o último caso de teste para imprimir uma linha em branco separadora
    # Exemplo: se caso = 0 e N = 2, caso < 1 é Verdadeiro -> imprime linha em branco
    if caso < N - 1:
        print()