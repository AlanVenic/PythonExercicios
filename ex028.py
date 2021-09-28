import random
from time import sleep
#Escreva um programa que faça o computador pensar em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O computador deve escrever na tela se o usuário acertou ou não

num = int(input('Adivinhe qual número estou pensando entre 0 e 5... '))
print('PROCESSANDO...')
sleep(2)
roll = random.randint(0, 5)
if num == roll:
    print('Você acertou! Eu pensei no {}!'.format(roll))
else:
    print('Você errou! Eu pensei no {}!'.format(roll))

num2 = int(input('Escolha um número e depois role dois dados! Você vence se acertar o resultado! '))
roll = random.randint(1, 6)
roll2 = random.randint(1, 6)
print('Rolando dois dados. O primeiro dado foi {}, o segundo dado foi {}!'.format(roll, roll2))
res = roll + roll2
if num == res:
    print('Você acertou! O resultado da rolagem foi {}!'.format(res))
else:
    print('Você errou! O resultado da rolagem foi {}!'.format(res))
