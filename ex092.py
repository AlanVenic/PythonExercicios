#crie um programa q leia nome, ano de nascimento e carteira de trabalho, e cadastre-os (com idade)
#num dicionario se por acaso a CTPS for diferente de ZERO, o dicionario recebera tambem o ano de
#contratação e salario. calcule e acrescente, alem da idade, com qnts anos a pessoa vai se aposentar
#obs: 35 anos de contribuição para se aposentar

from datetime import date

INSS = {}
INSS['nome'] = str(input('Digite seu nome: '))
ano = int(input('Digite seu ano de nascimento: '))
INSS['idade'] = date.today().year - ano
INSS['ctps'] = int(input('Digite sua CTPS [0 se não tiver]: '))
if INSS['ctps'] != 0:
    INSS['contrato'] = int(input('Qual o ano de contratação: '))
    apos = (INSS['contrato'] + 35) - ano
    INSS['salario'] = float(input('Qual seu salário: R$ '))
    print(f'nome: {INSS["nome"]} \n'
          f'idade: {INSS["idade"]} anos \n'
          f'CTPS: {INSS["ctps"]} \n'
          f'salário: R${INSS["salario"]:.2f} \n'
          f'Você irá se aposentar com {apos} anos')
else:
    print(f'nome: {INSS["nome"]} \n'
          f'idade: {INSS["idade"]} anos')
