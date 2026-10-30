#Crie uma pilha chamada historico_navegador.
historico_navegador = []

#Adicione as seguintes páginas, uma de cada vez: "google.com", "github.com" e "stackoverflow.com".
historico_navegador.append("google.com")
historico_navegador.append("github.com")
historico_navegador.append("stackoverflow.com")

#Simule o clique no botão "Voltar" removendo o último site visitado e imprima na tela qual site foi fechado.
removendosite = historico_navegador.pop()

print("O site removido foi: ", removendosite)

#Imprima na tela qual é a página em que o usuário está no momento (o novo topo da pilha).
removendosite2 = historico_navegador[-1]
print("Site que vc está no momento e o ", removendosite2)