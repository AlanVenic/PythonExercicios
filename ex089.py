#crie um programa q leia nome e 2 notas de varios alunos e guarde td numa lista composta.
#no final, mostre um boletim com a media de cada um e permita q o usuario possa mostrar as notas individualmente
#lista1=alunos>lista2=aluno+notas>lista3=notas

ficha = []

print('CADASTRO DE MÉDIAS')
while True:
    nome = str(input('Nome do aluno: '))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    cont = str(input('Deseja continuar?[S/N] ')).upper()
    if cont == 'N':
        break

print('BOLETIM DA TURMA A')
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}.')
vernot = str(input('Deseja ver as notas de algum aluno?[S/N] ')).upper()
if vernot == 'S':
    nomenot = str(input('De qual aluno deseja saber as notas? ')).lower()
    for nome in ficha:
        if nome[0] == nomenot:
           print(f'As notas de {nome[0]} foram: {nome[1]}')
           break
else:
    print('Obrigado, volte sempre')
