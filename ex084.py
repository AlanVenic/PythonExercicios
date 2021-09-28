#faça um proggrama q leia o nome e peso de varias pessoas, guardando td numa lista.
# no final, mostre: qnts pessoas foram cadastradas; uma listagem com as pessoas mais pesadas 100+;
#uma listagem com as pessoas mais leves 60-

cadastro = []
dados = []

while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    dados.append(cadastro[:])
    cadastro.clear()
    cont = str(input('Deseja continuar?[S/N] ')).upper()
    if cont == 'N':
        break
print(dados)
for p in dados:
    if p[1] >= 80:
        print(f'{p[0]} é um dos mais pesados com {p[1]}kg.')
for p in dados:
    if p[1] <= 60:
        print(f'{p[0]} é um dos mais leves com {p[1]}kg.')
print(f'O total de pessoas cadastradas foi {len(dados)}.')

