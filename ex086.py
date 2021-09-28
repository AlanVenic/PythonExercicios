#crie um programa q crie uma matriz de dimensão 3x3 em uma lista e preencha com valores digitados
#no final, mostre a matriz na tela com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

l1 = []
l2 = []
l3 = []
matriz = []

for n in range(0, 3):
    c = int(input('Digite um valor: '))
    l1.append(c)
for n in range(0, 3):
    c = int(input('Digite um valor: '))
    l2.append(c)
for n in range(0, 3):
    c = int(input('Digite um valor: '))
    l3.append(c)
matriz.append(l1)
matriz.append(l2)
matriz.append(l3)
print(matriz[0])
print(matriz[1])
print(matriz[2])
