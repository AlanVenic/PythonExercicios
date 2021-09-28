#crie um programa q mostre na tela todos os numeros pares num intervalo de 1 a 50

print('Quer saber os números pares num dado intervalo?')
inicio = int(input('Digite onde devo começar a contagem: '))
fim = int(input('Digite ate onde devo ir: '))

if inicio % 2 == 0:
    for c in range(inicio, fim +1, 2):
        print(c, end=' ')
else:
    for c in range(inicio +1, fim +1, 2):
        print(c, end=' ')
print('Fim')
