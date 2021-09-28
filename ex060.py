#faça um programa q leia um numero e mostre seu fatorial
#ex: 5!=5*4*3*2*1=120

from math import factorial
print('VAMOS CALCULAR O FATORIAL!')
num = int(input('Digite um número: '))
fat = 1
for c in range(1, num+1):
    fat = fat * c
print('O fatorial de {} é {}.'.format(num, fat))

n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))