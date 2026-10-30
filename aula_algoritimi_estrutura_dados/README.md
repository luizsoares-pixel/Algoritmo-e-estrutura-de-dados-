# Algoritmos e Estruturas de Dados

Repositório com exercícios e exemplos práticos usados nas aulas de
Algoritmos e Estruturas de Dados. Cada pasta `AulaXX` contém scripts
em Python com problemas resolvidos e atividades.

Estrutura
- **Aula01**: Exercícios introdutórios sobre busca e pilha.
	- `1025.py` — busca em vetor (uso de bisect para pesquisa binária).
	- `AtividadePilha.py` — verificação de balanceamento de parênteses (pilha).
- **Aula02**: Filas e simulações de procedimentos circulares.
	- `AtividadeFila.py` — simulação de descarte de cartas com `deque`.
	- `AtividadeKM.py` — eliminação circular / contadores (simulação de passos k/m).
- **Aula03**: Ordenação e processamento de listas.
	- `1162.py` — contagem de trocas em ordenação por inserção (problema de 'train swapping').
	- `1211.py` — cálculo de prefixos comuns entre strings (economia de dígitos/telefones).
- **Aula4**: Hashing e ordenações customizadas.
	- `Hash.py` — exemplo de tabela hash por resto (módulo) e agrupamento.
	- `OrdenacaoLambda.py` — ordenação por frequência e chave composta com `lambda`.
	- `OrdenacaoTamanho.py` — ordenação de palavras por tamanho (ordem decrescente).

Como executar
- Recomendado: usar Python 3.8+.
- Exemplo (Windows / PowerShell):

```powershell
python Aula01\1025.py
python Aula4\OrdenacaoLambda.py
```

Notas rápidas
- Cada arquivo lê da entrada padrão (`input()`); para testar, forneça os dados
	conforme o enunciado do respectivo problema ou redirecione um arquivo de testes.
- Os nomes dos arquivos refletem o problema ou o tópico; abra o script para ver
	o formato exato de entrada/saída.

Contribuições
- Se quiser adicionar soluções ou melhorias, faça um fork, crie uma branch
	e abra um pull request com uma breve descrição das alterações.

Licença
- Use conforme orientação do curso.

