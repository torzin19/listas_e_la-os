# Lista de nomes para gerar a mesma saída do slide
nomes = ["Marcelo", "Laura", "Maria", "João"]

# Percorre a lista obtendo tanto o índice (i) quanto o valor (nome)
for i, nomes in enumerate (nomes):
    print(i,nomes)


    print('----------------------------------------------')  

    
nomes = ["Marcelo", "Laura", "Maria", "João"]

# Percorre a lista obtendo tanto o índice (i) quanto o valor (nome)
for i in range(len(nomes)):
    print(i, nomes[i])