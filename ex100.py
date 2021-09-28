#faça um programa q tenha uma lista chamada numeros e duas funções chamadas sorteio() e somaPar()
#a primeira função vai sortear 5 numeros e coloca-los na lista. a segunda função vai mostrar a
#soma de tds os valores pares sorteados na função anterior

from random import randint
from time import sleep

numeros = []

def sorteio():
    for n in range(1, 6):
        n = randint(1, 10)
        print(n, end=' ')
        sleep(0.5)
        numeros.append(n)


def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(soma)

print('Sorteando 5 números: ', end='')
sorteio()
print()
print('A soma dos números pares sorteados é: ', end='')
somaPar()
