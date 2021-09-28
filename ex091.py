#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios
#guarde esses resultados num dicionario. no final, coloque esse dicionario em ordem, sabendo q o
#vencedor é quem tirou o maior valor no dado

from random import randint
from time import sleep
from operator import itemgetter

roll = {}
roll = {'Jogador 1': (randint(1, 6) + randint(1, 6)),
'Jogador 2': (randint(1, 6) + randint(1, 6)),
'Jogador 3': (randint(1, 6) + randint(1, 6)),
'Jogador 4': (randint(1, 6) + randint(1, 6))}
ranking = {}
print('VALORES SORTEADOS')
for k, v in roll.items():
    print(f'{k} tirou {v} na rolagem de 2 dados.')
    sleep(1)
ranking = sorted(roll.items(), key=itemgetter(1), reverse=True)
print('ORDEM DE VITÓRIA')
for i, n in enumerate(ranking):
    print(f'{i+1}º lugar: {n[0]} com {n[1]} pontos')
    sleep(1)