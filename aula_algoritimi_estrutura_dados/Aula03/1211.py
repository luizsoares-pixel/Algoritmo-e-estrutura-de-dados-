"""
===============================================================================
OBJETIVO DO DESAFIO (Beecrowd 1211 - Lista Telefônica Econômica):
===============================================================================
O problema pede para calcular a quantidade máxima de caracteres (dígitos) que 
podem ser economizados na impressão de uma lista de telefones. 

Regras:
1. Ao imprimir uma lista, a partir do segundo número, se os dígitos iniciais 
   (prefixo) forem exatamente iguais aos do número impresso imediatamente acima, 
   esses dígitos iniciais coincidentes podem ser omitidos.
2. Para maximizar a economia de caracteres, a lista de números deve ser ordenada 
   lexicograficamente (em ordem alfabética/crescente de strings) antes da comparação, 
   agrupando números com prefixos semelhantes lado a lado.
3. A entrada possui múltiplos casos de teste e encerra ao atingir o final do 
   arquivo (EOF - End Of File).

===============================================================================
EXEMPLO PRÁTICO RASTREADO PASSO A PASSO:
===============================================================================
Exemplo de Entrada:
------------------
2
12345
12354
3
535456
535488
835456

Rastreamento na Memória:
-----------------------
[Caso de Teste 1]
- Lendo N = 2
- Lista lida: telefones = ["12345", "12354"]
- Ordenação (telefones.sort()): ["12345", "12354"] (já ordenado)
- Inicializa economia = 0

* Iteração i = 1:
  - anterior = "12345"
  - atual    = "12354"
  - Comparação caractere a caractere (j):
    * j = 0: '1' == '1' -> continua (j = 1)
    * j = 1: '2' == '2' -> continua (j = 2)
    * j = 2: '3' == '3' -> continua (j = 3)
    * j = 3: '5' != '4' -> para o laço!
  - Caracteres iguais encontrados: j = 3
  - Atualiza economia = 0 + 3 = 3

- Saída gerada para Caso 1: 3

-----------------------
[Caso de Teste 2]
- Lendo N = 3
- Lista lida: telefones = ["535456", "535488", "835456"]
- Ordenação (telefones.sort()): ["535456", "535488", "835456"] (já ordenado)
- Inicializa economia = 0

* Iteração i = 1:
  - anterior = "535456"
  - atual    = "535488"
  - Comparação caractere a caractere (j):
    * j = 0: '5' == '5' -> continua (j = 1)
    * j = 1: '3' == '3' -> continua (j = 2)
    * j = 2: '5' == '5' -> continua (j = 3)
    * j = 3: '4' == '4' -> continua (j = 4)
    * j = 4: '8' != '5' -> para o laço!
  - Caracteres iguais encontrados: j = 4
  - Atualiza economia = 0 + 4 = 4

* Iteração i = 2:
  - anterior = "535488"
  - atual    = "835456"
  - Comparação caractere a caractere (j):
    * j = 0: '8' != '5' -> para o laço imediatamente!
  - Caracteres iguais encontrados: j = 0
  - Atualiza economia = 4 + 0 = 4

- Saída gerada para Caso 2: 4

-----------------------
CONDIÇÃO DE PARADA DO PROGRAMA:
-----------------------
- O laço 'while True' tenta ler 'input()' a cada iteração de caso de teste.
- Quando o arquivo de entrada termina e não há mais dados para ler, a função 
  input() dispara uma exceção 'EOFError'.
- O bloco 'except EOFError' captura essa exceção e executa o comando 'break', 
  encerrando o programa de forma limpa.
===============================================================================
"""

# Laço principal para processar múltiplos casos de teste até o fim do arquivo (EOF)
while True:
    try:
        # Lê a quantidade de números de telefone para o caso de teste atual
        # Exemplo: input() -> "2", n = 2
        n = int(input())
    except EOFError:
        # Interrompe o laço principal quando não houver mais linhas de entrada (Final do Arquivo)
        break

    # Lista responsável por armazenar todos os números de telefone do caso de teste
    telefones = []

    # Laço de repetição para ler os 'n' números de telefone da entrada
    for _ in range(n):
        # Lê o telefone, remove espaços em branco adicionais/quebras de linha com strip() e adiciona à lista
        # Exemplo: input().strip() -> "12345"
        telefones.append(input().strip())

    # Ordena os telefones em ordem lexicográfica (alfabética/crescente)
    # Isso garante que telefones com prefixos iguais fiquem adjacentes na lista para maximizar a economia
    # Exemplo: ["835456", "535456"] -> ["535456", "835456"]
    telefones.sort()

    # Variável acumuladora para guardar o total de caracteres economizados
    economia = 0

    # Percorre os telefones da lista a partir do segundo elemento (índice 1) até o último (índice n - 1)
    for i in range(1, n):
        # Obtém o telefone da posição anterior na lista ordenada
        # Exemplo: se i = 1, anterior = telefones[0] ("535456")
        anterior = telefones[i - 1]
        
        # Obtém o telefone da posição atual na lista ordenada
        # Exemplo: se i = 1, atual = telefones[1] ("535488")
        atual = telefones[i]

        # Ponteiro/Índice 'j' usado para comparar os caracteres dos dois telefones posição por posição
        j = 0

        # Percorre os caracteres de ambos os telefones enquanto o índice for válido e os caracteres forem idênticos
        # Exemplo: compara '5' com '5', '3' com '3', etc.
        while j < len(atual) and atual[j] == anterior[j]:
            # Avança para o próximo caractere se forem iguais
            j += 1

        # Adiciona a quantidade de caracteres prefixos idênticos encontrados ao total economizado
        # Exemplo: j = 4 prefixos iguais -> economia += 4
        economia += j

    # Exibe o total final de caracteres economizados para o caso de teste atual
    # Exemplo: print(4)
    print(economia)