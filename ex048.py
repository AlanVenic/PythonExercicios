#faça um progrma q calcule a soma de numeros impares multiplos
#de 3 e que se encontram num intervalo de 1 a 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} números é {}'.format(cont, soma))

