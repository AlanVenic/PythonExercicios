num = int(input('Digite um número de 0 a 9999: '))
uni = num % 10
print('A unidade é: {:.0f}' .format(uni))
num = (num - uni)/10
dez = num % 10
print('A dezena é: {:.0f}' .format(dez))
num = (num - dez)/10
cen = num % 10
print('A centena é: {:.0f}' .format(cen))
num = (num - cen)/10
print('A milhar é: {:.0f}' .format(num))
