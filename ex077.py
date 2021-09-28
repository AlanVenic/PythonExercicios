#crie um programa q tenha uma tupla com varias palavras (nao acentuar). depois,
#voce deve mostrar, para cada palavra, quais sao as suas vogais
pws = ('Jace', 'Liliana', 'Ajani', 'Garruk', 'Chandra',
       'Nicol Bolas', 'Karn', 'Ugin', 'Teferi', 'Nissa', 'Gideon', 'Narset')

for c in pws:
    print(f'As vogais no nome {c} são: ', end='')
    for i in range(0, len(c)):
        if c[i] in 'YyAaEeIiOoUu':
            print(c[i], end=' ')
    print('', end='\n')



