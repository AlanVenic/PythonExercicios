#refaça o desafio009 mostrando a tabuada
#de um numero q o usuario escolheu, utilizando o 'for'

print('Quer saber a tabuada de um número?')
num = int(input('Digite um número: '))

print('A tabuada do número {} é:'.format(num))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))