#desenvolva um programa q leia nome, idade e sexo de 4 pessoas
#no final, mostre:
# media de idade do grupo;
# nome do homem mais velho;
# qnts mulheres tem menos de 20 anos

nomevelho = ''
idadevelho = 0
mulheres20 = 0
media = 0

print('CADASTRO DE PESSOAS')
print('Digite o nome, idade e sexo da pessoa a ser cadastrada.')
for c in range(1, 5):
    print('{}ª PESSOA'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper().strip()
    media += idade
    if sexo == 'M' and idadevelho < idade:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
print('O homem mais velho tem {} anos e se chama {}.'.format(idadevelho, nomevelho))
print('Existem {} mulheres com menos de 20 anos.'.format(mulheres20))
print('A média de idade do grupo é {}.'.format(media / 4))
