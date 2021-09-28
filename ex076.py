#crie um programa q tenha uma tupla unica com nomes de produtos e seus
#respectivos preços em sequencia. no final, mostre a listagem de preços
#organizando os dados em forma tabular


produtos = ('Caneta', 2, 'Lapis', 1, 'Borracha', 1.50, 'Caderno', 15.90, 'Módulo', 65.50, 'Papel (100 folhas)', 30,
            'Pincel', 4.50, 'Tinta', 3.90, 'Cartolina', 0.80, 'Lancheira', 25.90)
e = ''
print('LISTA DE PRODUTOS')
print(f'PRODUTO{e:<18}PREÇO')
for p, c in enumerate(produtos):
    if (p % 2) == 0:
        print(f'{c:.<25}', end='')
    else:
        print(f'R$ {c:>4.2f}')

