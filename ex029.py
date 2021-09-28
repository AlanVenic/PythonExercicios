#Escreva um programa que leia a velocidade de um carro.
# Se ela ultrapassar 80km/h, mostre uma pensagem dizendo que foi multado
#A multa vai custar R$7,00 por cada km acima do limite
import random

corre = str(input('Você está andando na rodovia e a pista está livre. Você acelera? Responda sim ou não: '))
radar = random.randint(1, 2)
if radar == 1:
    print('Havia um radar na rodovia!')
if radar == 2:
    print('Não havia radares na via!')
if corre == 'sim':
    vel = random.randint(81, 180)
    multa = (vel - 80)*7
    if radar == 1:
        print('Você estava a {}km/h e foi multado em R${:.2f}!'.format(vel, multa))
    if radar == 2:
        print('Você passou na rodovia a {}km/h, por sorte não havia radares ou você seria multado em R${:.2f}...'.format(vel, multa))
if corre == 'não':
    vel2 = random.randint(40, 80)
    if radar == 1:
        print('Você estava a {}km/h. Ainda bem que você estava no limite...'.format(vel2))
    if radar == 2:
        print('Você estava a {}km/h. Dirija com segurança!'.format(vel2))