#desenvolva um programa que pergunte a distancia de uma viagem em km.
# calcule o preço da passagem, cobrando R$0,50 por km da viagem de ate
# 200km e R$0,45 para viagens mais longas

viagem = int(input('Qual a distância do seu destino? '))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45

print('O preço da sua viagem de {:.0f}km é R${:.2f}'.format(viagem, preço))
