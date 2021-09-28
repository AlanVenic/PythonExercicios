#crie um programa q leia ano de nascimento de 7 pessoas
#no final, mostre qnts pessoas ainda não atingiram a maioridade e
#qnts são maiores de idade (21 anos)

from datetime import date

maiores = 0
menores = 0
print('SER ADULTO É UMA DROGA')
print('Será que você já é adulto?')
for c in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade <= 21:
        maiores += 1
    else:
        menores += 1
print('Nessa lista, {} pessoas são maiores de idade e {} são menores de idade.'.format(maiores, menores))
