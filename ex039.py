#faça um programa q leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
#-se ele ainda vai se alistar no serviço militar
#se já é a hora de se alistar
#se já passou da hora de se alistar
#o programa tambem deve mostrar o tempo q falta ou q passou do prazo

from datetime import date
print('Será que está na hora de fazer o seu alistamento militar obrigatório?')
ano = int(input('Qual seu ano de nascimento? '))

idade = date.today().year - ano

if idade == 18:
    print('Você já tem {} anos, está na hora de você se alistar!'.format(idade))
elif idade < 18:
    print('Faltam {} anos para o seu alistamento obrigatório!'.format(18 - idade))
    print('Seu alistamento será no ano de {}.'.format(ano + 18))
else:
    print('Você está {} anos atrasado no seu alistamento militar!'.format(idade - 18))
    print('Seu alistamento foi no ano de {}.'.format(ano + 18))



