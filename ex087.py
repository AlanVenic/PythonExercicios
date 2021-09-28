#aprimore o exercicio 86 mostrando no final: a soma de tds os valores pares;
#a soma dos valores da terceira coluna; o maior valor da segmatriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'A soma dos pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')