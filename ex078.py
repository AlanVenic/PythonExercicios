#faça um programa q leia 5 numeros digitados e guarde-os numa lista.
#no final, mostre qual o maior e qual o menor valor digitados e suas respectivas posições
#obs: indicar se o valor aparecer mais de 1x

num = []
maior = 0
menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'O maior valor é {maior} que foi encontrado nas posições', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i} ', end='')
print(f'\nO menor valor é {menor} que foi encontrado nas posições', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i} ', end='')
