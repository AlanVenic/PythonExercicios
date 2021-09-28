#melhore o jogo do desafio 028 onde o computador pensa um numero entre 0 e 10
#so q agora o jogador vai tentar adivinhar ate acertar, mostrando no final qnts
#palpites foram necessarios para vencer.

from time import sleep
from random import randint

tent = 0
num = 0
roll = randint(1, 1000)
print('Adivinhe qual número eu pensei entre 1 e 1000... ')
while roll != num:
    tent += 1
    num = int(input('Digite um valor: '))
    print('PROCESSANDO...')
    sleep(0.5)
    if num == roll:
        print('Você acertou! Eu pensei no {}!'.format(roll))
    elif num > roll:
        print('Menos... tente de novo.')
    elif num < roll:
        print('Mais... tente outra vez.')
    else:
        print('Você errou! tente de novo!')
if tent == 1:
    print('Você acertou de primeira! PARABÉNS!')
else:
    print('Você precisou de {} tentativas para acertar!'.format(tent))
