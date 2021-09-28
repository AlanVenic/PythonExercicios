#faça um programa q leia um numero inteiro e diga se ele é um numero primo
#divisivel por 1 e por ele msm apenas

print('Será que o número escolhido é primo?')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('O número escolhido é primo.')
else:
    print('O número escolhido não é primo.')
