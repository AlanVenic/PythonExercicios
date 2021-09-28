#crie um programa q leia nome, sexo e idade de varias pessoas. guardando os dados de cada um num dicionario
#e tds os dicionarios em uma lista. no final, mostre: qnts pessoas foram cadastradas; a media de idade do grupo;
#uma lista com as mulheres; uma lista com tds as pessoas com idade acima da média

dados = {}
pessoas = []
soma = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo[F/M]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Opção inválida. Digite apenas M ou F')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        cont = str(input('Deseja continuar?[S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('Opção inválida. Digite apenas S ou N')
    if cont == 'N':
        break

media = soma / len(pessoas)
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade do grupo é de {media:.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'As pessoas cadastradas com idade acima da média são:')
for p in pessoas:
    if p['idade'] >= media:
        print(f'{p["nome"]} com {p["idade"]} anos', end=' ')
    print()
print('FIM DO PROGRAMA')