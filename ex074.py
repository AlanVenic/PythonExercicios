#crie um programa q gere 5 numeros aleatorios de 0 a 10 e coloque em uma tupla
#depois, mostre a listagem de numeros gerados e indique o menor e o maior valor da tupla

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for c in numeros:
    print(c)

ordem = sorted(numeros)

print(f'O menor valor rolado foi {ordem[0]} e o maior foi {ordem[-1]}')
print(f'O menor valor rolado foi {min(numeros)} e o maior foi {max(numeros)}')
