#desenvolva uma logica q leia o peso e altura. calcule o IMC e mostre seu status de acorod com a tabela
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#entre 25.1 e 30: sobrepeso
#entre 30.1 e 40: obesidade
#acima de 40: obesidade morbida

print('Será que você está no seu peso ideal? Vamos calcular seu IMC e descobrir!')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilos: '))

imc = peso/(altura**2)
ideal1 = 18.5*(altura**2)
ideal2 = 25*(altura**2)

if imc < 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do seu peso ideal '
          'que é de {:.1f}kg a {:.1f}kg'.format(imc, ideal1, ideal2))
elif imc <= 24.9:
    print('Seu IMC é {:.1f}. Você está na sua faixa de peso ideal '
          'que é de {:.1f}kg a {:.1f}kg.'.format(imc, ideal1, ideal2))
elif imc <= 29.9:
    print('Seu IMC é {:.1f}. Você está com sobrepeso pois seu peso '
          'ideal é de {:.1f}kg a {:.1f}kg.'.format(imc, ideal1, ideal2))
elif imc <= 39.9:
    print('Seu IMC é {:.1f}. Você está obeso pois seu peso ideal é '
          'de {:.1f}kg a {:.1f}kg.'.format(imc, ideal1, ideal2))
else:
    print('Seu IMC é {:.1f}. Você está com obesidade morbida pois '
          'seu peso ideal é de {:.1f}kg a {:.1f}kg.'.format(imc, ideal1, ideal2))
