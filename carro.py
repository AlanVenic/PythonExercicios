from datetime import date
hj = date.today().year
print('Quanto será que vale seu carro? Me diga as informações sobre ele e vamos descobrir seu valor atual.')
novo = float(input('Qual o preço da versão atual do seu carro? '))
ano = int(input(('Qual o ano do seu carro? ')))
if ano <= 1990:
    antigo = str(input('Seu carro é uma antiguidade (sim ou não)? '))
km = float(input('Qual a quilometragem do seu carro? '))
ava = int(input(('Quantas avarias o seu carro tem? ')))
rev = str(input('Você fez todas as revisões corretamente (sim ou não)? '))

rev = rev.lower()
descKm = km/10000
descRev = 0
idade = hj - ano
descIda = 15

if idade < 20:
    descIda = descIda+(idade*1.8)
else:
    descIda = descIda+(idade*1.4)
if km > 100000:
    descKm = descKm+((km-100000)/20000)
descAva = ava*3
if rev == 'não':
    descRev = 10
final = novo - novo*((descIda+descKm+descAva+descRev)/100)
reliquia = (1970 - ano)*10
finalAnt = novo - novo*((descKm+descAva+descRev)/100)
finalRel = finalAnt + (novo*reliquia)/100
if (antigo == 'sim') and (ano < 1970):
    print('O preço atual do seu carro é {}R${:.2f}{}.'.format('\033[1;32m', finalRel, '\033[m'))
elif (antigo == 'sim') and (ano >= 1970):
    print('O preço atual do seu carro é {}R${:.2f}{}.'.format('\033[1;32m', finalAnt, '\033[m'))
elif final >= novo/2:
    print('O preço atual do seu carro é {}R${:.2f}{}.'.format('\033[1;32m', final, '\033[m'))
elif final <= 0:
    print('Infelizmente, devido as condições do seu carro, ele não possui valor de mercado!')
else:
    print('O preço atual do seu carro é {}R${:.2f}{}.'.format('\033[1;31m', final, '\033[m'))
