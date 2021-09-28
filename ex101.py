#crie um programa q tenha ua função chamada voto() q receba como parametro o ano de nascimento
#de uma pessoa e retorne um valor literal, indicando se a pessoa tem voto negado(15ou-), opcional(16-17, 65+)
# ou obrigatorio(18-64) nas proximas eleiçoes

from datetime import date


def voto(a):
    ano = a
    idade = date.today().year - ano
    if idade <= 15:
        print(f'Você tem {idade} anos e não pode votar.')
    elif idade <= 17 or idade >= 65:
        print(f'Você tem {idade} anos e o voto é OPCIONAL.')
    else:
        print(f'Você tem {idade} anos e o voto é OBRIGATÓRIO.')


print('ANO ELEITORAL')
eleitor = int(input('Qual seu ano de nascimento? '))

voto(eleitor)
