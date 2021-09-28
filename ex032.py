from datetime import date
#faça um programa que diga se um ano é bissexto

ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
