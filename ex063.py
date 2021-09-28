#escreva um programa q leia um numero 'n' inteiro e mostre na tela os 'n'
#primeiros elementos de uma sequencia de fibonacci

print('SEQUENCIA DE FIBONACCI')
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite o segundo termo: '))
term = int(input("Quantos termos deseja mostrar: "))
print('{} - {} '.format(n1, n2), end='')
cont = 3
while cont <= term:
    n3 = n1 + n2
    print('- {} '.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' - FIM')
