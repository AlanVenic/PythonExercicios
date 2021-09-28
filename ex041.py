#a confederação nacional de natação precisa de um programa que
#leia o ano de nascimento do atleta e mostre sua categoria de acordo cmo idade:

from datetime import date
ano = int(input('Olá atleta! Digite seu ano de nascimento para sabermos a qual categoria você pertence: '))

idade = date.today().year - ano

if idade <= 9:
    print('Você tem {} anos e está na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e está na categoria JUNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e está na categoria SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos e está na categoria MASTER!'.format(idade))


