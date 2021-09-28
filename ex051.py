#desenvolva um programa q leia o primeiro termo e a razão de uma progressão aritmetica
#no final, mostre os 10 primeiros termos dessa progressão

print('Quer saber os 10 primeiros termos de uma progressão aritmética?')
term = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão da progressão: '))
dez = term + (10 - 1) * raz
print('A progressão aritmética de {} com a razão {} é:'.format(term, raz))
for c in range(term, dez + raz, raz):
    print('{}'.format(c), end=' ')