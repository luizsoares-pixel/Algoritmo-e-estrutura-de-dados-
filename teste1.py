# 1. Criamos uma pilha vazia
pilha = []

# 2. Empilhando livros (adicionando no topo)
livro1 = input(str("digite primeiro livro:"))
livro2 = input(str("digite segundo livro:"))
livro3 = input(str("digite terceiro livro:"))

pilha.append(livro1)
pilha.append(livro2)
pilha.append(livro3)

print("Sua pilha atual: ", pilha)
print('Caso queira tirar o ultimo livro escreva "sim", se não quiser "não"')

edicao = input(str("digite: "))

if edicao == "sim":
    
    # 3. Desempilhando (tirando do topo)
    livro_removido = pilha.pop()

    print("Você tirou:", livro_removido)

    # 4. Como ficou a pilha agora?
    print("Pilha depois da remoção:", pilha)

else :
    # 4. Como ficou a pilha agora?
    print("Pilha sem remoção", pilha)