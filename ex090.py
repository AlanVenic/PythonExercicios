#faça um progrma q leia nome e media de um aluno (digitado), guarde tambem a situação em um dicionario
#no final, mostre o conteudo da estrutura em tela

aluno = {}
print('SITUAÇÃO DO ALUNO')
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input('Digite a média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print(f'O aluno {aluno["nome"]} está {aluno["situação"]} pois obteve média {aluno["média"]}')
