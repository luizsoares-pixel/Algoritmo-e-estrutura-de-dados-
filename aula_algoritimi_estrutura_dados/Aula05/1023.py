"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1023 - Estiagem):
===============================================================================
O objetivo deste desafio é calcular o consumo de água por pessoa em imóveis de 
uma cidade e determinar a média geral de consumo por habitante.

Regras:
1. Para cada imóvel, é informada a quantidade de moradores (X) e o consumo total 
   do imóvel em m³ (Y).
2. O consumo por pessoa de um imóvel é truncado/arredondado para baixo 
   (divisão inteira: Y // X).
3. Deve-se agrupar a quantidade total de pessoas por cada valor de consumo 
   truncado por pessoa.
4. A lista de moradores agrupados deve ser exibida em ordem ASCENDENTE do consumo 
   por pessoa no formato "quantidade_de_pessoas-consumo_por_pessoa".
5. Deve-se calcular o consumo médio real por habitante da cidade inteira:
   (soma de todo o consumo Y) / (soma de todas as pessoas X).
   O resultado deve ser formatado com 2 casas decimais SEM arredondamento (truncado).
6. Deve-se imprimir uma linha em branco entre dois casos de teste consecutivos.
7. A condição de parada ocorre quando a quantidade de imóveis N for igual a 0.

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
3
3 22
2 11
3 39
5
1 25
2 20
3 31
2 40
6 70
2
1 1
3 2
0

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Contador: caso = 1
- Lendo N = 3
- Inicializa 'consumo = {}', 'totalpessoas = 0', 'totalconsumo = 0'

* Imóvel 1: pessoas = 3, quantidade = 22
  - totalpessoas = 0 + 3 = 3
  - totalconsumo = 0 + 22 = 22
  - consumoporpessoa = 22 // 3 = 7
  - consumo[7] = 3

* Imóvel 2: pessoas = 2, quantidade = 11
  - totalpessoas = 3 + 2 = 5
  - totalconsumo = 22 + 11 = 33
  - consumoporpessoa = 11 // 2 = 5
  - consumo[5] = 2

* Imóvel 3: pessoas = 3, quantidade = 39
  - totalpessoas = 5 + 3 = 8
  - totalconsumo = 33 + 39 = 72
  - consumoporpessoa = 39 // 3 = 13
  - consumo[13] = 3

- Ordenação das chaves em consumo (sorted(consumo.items())):
  valores = [(5, 2), (7, 3), (13, 3)]

- Construção da lista formatada:
  * (5, 2)  -> "2-5"
  * (7, 3)  -> "3-7"
  * (13, 3) -> "3-13"

- Cálculo da média real:
  media = 72 / 8 = 9.00

- Saída gerada:
  Cidade# 1:
  2-5 3-7 3-13
  Consumo medio: 9.00 m3.

- Imprime linha em branco e incrementa caso = 2.

-----------------------
[Caso de Teste 2]
- Lendo N = 5
- Processando os 5 imóveis:
  * 1 25 -> consumoporpessoa = 25 // 1 = 25 (1 pessoa)
  * 2 20 -> consumoporpessoa = 20 // 2 = 10 (2 pessoas)
  * 3 31 -> consumoporpessoa = 31 // 3 = 10 (3 pessoas -> total para consumo 10 = 2 + 3 = 5 pessoas)
  * 2 40 -> consumoporpessoa = 40 // 2 = 20 (2 pessoas)
  * 6 70 -> consumoporpessoa = 70 // 6 = 11 (6 pessoas)

- totalpessoas = 1 + 2 + 3 + 2 + 6 = 14
- totalconsumo = 25 + 20 + 31 + 40 + 70 = 186
- Dicionário agrupado e ordenado: [(10, 5), (11, 6), (20, 2), (25, 1)]

- Cálculo da média real:
  media = 186 / 14 = 13.285714...
  (com 2 casas decimais truncadas/formatadas: 13.28)

- Saída gerada:
  Cidade# 2:
  5-10 6-11 2-20 1-25
  Consumo medio: 13.28 m3.

- Imprime linha em branco e incrementa caso = 3.

-----------------------
[Caso de Teste 3]
- Lendo N = 2
- Imóveis:
  * 1 1 -> consumoporpessoa = 1 // 1 = 1 (1 pessoa)
  * 3 2 -> consumoporpessoa = 2 // 3 = 0 (3 pessoas)
- totalpessoas = 4, totalconsumo = 3
- Ordenado: [(0, 3), (1, 1)]
- media = 3 / 4 = 0.75

- Saída gerada:
  Cidade# 3:
  3-0 1-1
  Consumo medio: 0.75 m3.

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O programa executa em um laço infinito 'while True'.
- A cada início do laço, lê o inteiro N.
- A condição 'if N == 0: break' encerra a execução do programa no momento em que 
  a quantidade N de imóveis informada for zero (0).
===============================================================================
"""

# Variável de controle para identificar o número sequencial do caso de teste (Cidade# 1, Cidade# 2, ...)
caso = 1 

# Laço principal para processar múltiplos casos de teste até encontrar o valor 0
while True:
    # Lê a quantidade de imóveis do caso de teste atual
    # Exemplo: input() -> "3", N = 3
    N = int(input())

    # Condição de parada: encerra o laço principal se N for igual a 0
    if N == 0:
        break

    # Dicionário para acumular a quantidade de pessoas por consumo truncado por pessoa
    # Estrutura: {consumo_truncado: total_de_pessoas}
    consumo = {}

    # Variáveis acumuladoras do total de moradores e do consumo total da cidade
    totalpessoas = 0 
    totalconsumo = 0

    # Laço para ler os dados de cada um dos N imóveis
    for _ in range(N):
        # Lê a quantidade de pessoas e o consumo total do imóvel
        # Exemplo: input() -> "3 22" -> pessoas = 3, quantidade = 22
        pessoas, quantidade = map(int, input().split())

        # Acumula o número de moradores e a quantidade de água consumida na cidade
        totalpessoas += pessoas
        totalconsumo += quantidade

        # Calcula o consumo individual por pessoa arredondado/truncado para baixo (divisão inteira //)
        # Exemplo: 22 // 3 = 7
        consumoporpessoa = quantidade // pessoas

        # Soma a quantidade de moradores ao grupo que possui o mesmo consumo truncado por pessoa
        # Exemplo: se já havia pessoas com consumo 7, soma mais 'pessoas'; caso contrário, inicia com 0 + 'pessoas'
        consumo[consumoporpessoa] = consumo.get(
            consumoporpessoa, 0
        ) + pessoas

    # Obtém uma lista de tuplas (consumo_por_pessoa, total_pessoas) ordenada em ordem crescente de consumo
    # Exemplo: [(5, 2), (7, 3), (13, 3)]
    valores = sorted(consumo.items())

    # Imprime o cabeçalho com o número sequencial da cidade
    # Exemplo: "Cidade# 1:"
    print(f"Cidade# {caso}:")

    # Lista auxiliar para armazenar as strings formatadas "pessoas-consumo"
    resultado = []

    # Itera sobre os pares ordenados de (consumo_por_pessoa, quantidade_de_pessoas)
    for consumomedio, pessoas in valores:
        # Formata a string "pessoas-consumo" e adiciona à lista de resultados
        # Exemplo: f"{2}-{5}" -> "2-5"
        resultado.append(
            f"{pessoas}-{consumomedio}"
        )
        
    # Imprime todas as combinações "pessoas-consumo" em uma única linha separadas por espaço
    # Exemplo: "2-5 3-7 3-13"
    print(" ".join(resultado))

    # Calcula a média real de consumo por pessoa dividindo o consumo total pelo total de pessoas
    # Exemplo: 72 / 8 = 9.0
    media = totalconsumo / totalpessoas

    # Imprime o consumo médio formatado com 2 casas decimais
    # Exemplo: "Consumo medio: 9.00 m3."
    print(f"Consumo medio: {media:.2f} m3.")

    # Imprime uma linha em branco para separar os casos de teste
    print()

    # Incrementa o número da cidade para o próximo caso de teste
    caso += 1