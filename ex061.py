#refaça o desafio 051, lendo o primeiro termo e a razão de uma PA.
#mostrando os 10 primeiros termos da PA usando while

print('Quer saber os 10 primeiros termos de uma progressão aritmética?')
term = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão da progressão: '))

cont = 1
while cont <= 10:
    print('{} > '.format(term), end=' ')
    term += raz
    cont += 1
print('FIM')
