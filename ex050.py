#desenvolva um programa q leia seis numeros inteiros
#e mostre a soma desses numeros que forem pares

print('SOMA DOS PARES')
print('Escolha seis números, farei a soma apenas dos que forem pares.')

cont = 0
soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n

print('A soma de {} números pares foi {}'.format(cont, soma))
