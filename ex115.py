#crie um sistema modularizado q permita cadastrar pessoas pelo nome e idade em um arquivo
#de texto simples. o sistema so vai ter 2 opções: cadastrar uma nova pessoa e listar tds as pessoas cadastradas

from utilidadesCEV.dados import *
from time import sleep
from arquivo import *

arq = 'cev.txt'

if not arqExist(arq):
    criarArq(arq)


while True:
    resp = menu(['Ver Cadastro de Pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        head('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resp == 3:
        head('Saindo do sistema...')
        break
    else:
        head('ERRO! Digite uma opção válida!')
    sleep(1)

