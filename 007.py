#GERANDO LISTAS DE NÚMEROS
import random # numeros aleatorios
numeros = [10, 67, 7, 4, 3, 2, 1 ,5, 6, 8, 9]
random.shuffle(numeros) #embaralha a lista
sorteado = numeros [0]
numeros.remove(sorteado)

print(f'número sorteado: {sorteado}')
print(f'lista atualizada: {numeros}')

print('----------------------------------------------------------------------------------------------------------------------------------------')

import random # numeros aleatorios
numeros = [0]
while len (numeros) <10:
    numero = random.randint(1, 100)
    if numero not in numeros:
        numeros.append(numero)

print(f'lista de numeros: {numeros}')