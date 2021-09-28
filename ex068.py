#faça um programa q jogue par ou impar com o usuario. o jogo so será
#interrompido qnd o jogador perder, mostrando o total de vitorias consecutivas no final
from random import randint
soma = parimpar = n = r = 0
while True:
    roll = randint(0, 5)
    escolha = int(input('[0] Par ou [1] Impar: '))
    while escolha >= 2:
        print('Valor inválido, escolha 0 ou 1.')
        escolha = int(input('[0] Par ou [1] Impar: '))
    n = int(input('Digite um valor de 0 a 5: '))
    while n > 5:
        print('Valor inválido, escolha um número entre 0 e 5!')
        n = int(input('Digite um valor de 0 a 5: '))
    soma = (roll + n)
    parimpar = soma % 2
    r += 1
    if escolha != parimpar:
        break
    print(f'O computador jogou {roll} e você {n}, o total deu {roll + n}, você ganhou!')
print(f'O computador jogou {roll} e você {n}, o total deu {roll + n}, você perdeu!')
print(f'Você venceu {r - 1} rodadas.')
