#crie um programa q leia idade e sexo de varias pessoas. a cada pessoa cadastrada
#o programa deve perguntar ao usuario se quer continuar. no final, mostre:
#qnts pessoas tem +18 anos; qnts homens foram cadastrados; qnts mulheres tem -20 anos

print('CADASTRO DE PESSOA FÍSICA')
n = homem = mulher20 = maiores = 0
while True:
    n += 1
    print(f'{n}ª pessoa')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    while sexo not in 'MF':
        print('Esta opção é inválida.')
        sexo = str(input('Sexo [F/M]: ')).strip().upper()
    print('Pessoa cadastrada com sucesso.')
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while cont not in 'SN':
        print('Esta opção é inválida.')
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if sexo == 'M':
        homem += 1
    if idade >= 18:
        maiores += 1
    if sexo == 'F':
        if idade <= 20:
            mulher20 += 1
    if cont == 'N':
        break
print(f'''Cadastro finalizado. 
Foram cadastrados {homem} homens.
Das pessoas cadastradas {maiores} são maiores de 18 anos.
Das mulheres cadastradas {mulher20} tem menos de 20 anos.''')




