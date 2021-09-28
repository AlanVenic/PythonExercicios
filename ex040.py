#crie um programa que leia duas notas de aluno e calcule sua media
#mostrando uma msg final de acordo com a media atingida

print('Verifique se você foi aprovado neste semestre.')
num1 = float(input('Digite sua primeira nota: '))
num2 = float(input('Digite sua segunda nota: '))

media = (num1 + num2)/2

if media < 5.0:
    print('Sua média foi {}. Você foi reprovado pois sua média está abaixo de 5.0.'.format(media))
elif media > 5.0 and media < 6.9:
    print('Sua média foi {}. Você está de recuperação pois sua média está abaixo de 7.0.'.format(media))
else:
    print('Sua média foi {}. Você foi aprovado pois sua média está acima de 7.0.'.format(media))