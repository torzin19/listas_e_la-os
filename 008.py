lista = [5, 2, 3, 4, 1]

for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(lista)

            numeros = [5, 2]

print(numeros[0] > numeros[1])
numeros = [5, 2]

if numeros[0] > numeros[1]:
    print("Precisa trocar")
    numeros = [5, 2, 3]

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]

print(numeros)

numeros = [5, 2, 3]

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
    print(numeros)

    numeros = [5,2,3,4,1]

for rodada in range(len(numeros)):
    for i in range(len(numeros) - 1):
        if numeros[i]> numeros[i+1]:
            numeros[i],numeros[i+1] = numeros[i+1], numeros[i]
        print(numeros)