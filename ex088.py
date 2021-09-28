#faça um programa q ajude um jogador da megasena a criar palpites. o programa vai perguntar qnts
#jogos serão gerados e vai sortear 6 numeros diferentes entre 1 e 60 para cada jogo, cadastrando td
#numa lista composta

from random import randint
from time import sleep

lista = []
jogos = []
cont = 0
print('JOGAR NA MEGASENA')
qnt = int(input('Quantos jogos devo sortear: '))
tot = 1
while tot <= qnt:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
jogos.sort()
print(f'SORTEANDO {qnt} JOGOS...')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)


jogo = []
palpites = []

final = int(input('Quantos palpites você quer gerar? '))
for x in range(0, final):
    roll = 0
    while roll != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            roll += 1
    palpites.append(jogo)
    print(sorted(palpites[x]))
    jogo = []
