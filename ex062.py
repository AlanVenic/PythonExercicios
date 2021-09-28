#melhore o desafio 61 perguntando ao usuario se ele quer mais alguns termos
#o programa encerra qnd ele disser q quer mostrar 0 termos

print('Quer saber os 10 primeiros termos de uma progressão aritmética?')
term = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão da progressão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(term), end=' ')
        term += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja mostrar a mais: '))
print('Razão finalizada com {} termos mostrados.'.format(total))

