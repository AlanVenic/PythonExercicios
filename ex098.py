#faça um programa com uma função chamad contador() com 3 parametros: inicio, fim e passo
#e realize a contagem: seu programa tem q realizar 3 contagens atraves da função criada
#de 1 ate 10, de 1 em 1; de 10 ate 0 de 2 em 2; contagem personalizada

from time import sleep

def contador(a, b, c):
    c = abs(c)
    if c == 0:
        c = 1
    elif a > b:
        c = -c
        for cont in range(a, b-1, c):
            print(cont, end=' ')
            sleep(0.5)
    elif a < b:
        for cont in range(a, b+1, c):
            print(cont, end=' ')
            sleep(0.5)
    print('FIM!')


print('O CONTADOR')
inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))
passo = int(input('Digite o passe de contagem: '))

contador(inicio, fim, passo)