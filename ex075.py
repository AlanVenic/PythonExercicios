#desenvolva um programa q leia 4 valores digitados e guarde-os numa tupla. depois mostre:
#qnts vezes apareceu o 9; em q posição foi digitado o primeiro 3; quais foram os numeros pares

num = (int(input('Digite o 1º valor: ')),
      int(input('Digite o 2º valor: ')),
      int(input('Digite o 3º valor: ')),
      int(input('Digite o 4º valor: ')))

print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro 3 apareceu na posição {num.index(3)+1}.')
else:
    print('O número 3 não aparece em nenhuma posição')
print(f'Os números pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
