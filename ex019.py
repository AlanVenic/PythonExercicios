from random import choice, shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
e = choice(lista)
shuffle(lista)
print('A ordem de apresentação será {}, {}, {}, {}'.format(lista[0], lista[1], lista[2], lista[3]))

