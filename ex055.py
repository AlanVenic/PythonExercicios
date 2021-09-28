#faça um programa q leia o peso de 5 pessoas. no final
#mostre qual o mais pesado e qual o mais leve

maior = 0
menor = 0

print('O GORDO E O MAGRO')
print('Diga o nome e peso de cada pessoa a ser avaliada.')
for c in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa mais pesada pesa {:.1f}kg.'.format(maior))
print('A pessoa mais leve pesa {:.1f}kg.'.format(menor))