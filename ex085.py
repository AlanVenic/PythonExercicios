#crie um programa onde o usuario possa digitar 7 valores e cadastre-os numa lista, mantendo separados
#valores pares e impares em duas listas dentro da lista valores. no final, mostre os valores
# pares e impares em ordem crescente

pares = []
impares = []
num = []

for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
num.append(pares[:])
num.append(impares[:])
print(f'pares={sorted(pares)}, impares={sorted(impares)}')
