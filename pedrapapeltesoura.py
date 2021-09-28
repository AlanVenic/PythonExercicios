#pedra>papel>tesoura>pedra
import random
jogo = str(input('Vamos jogar PEDRA, PAPEL OU TESOURA!\n'
                 'Escolha um: '))
cor = {'no':'\033[m',
     'bw':'\033[7m',
     'rb':'\033[31;45m',
     'gw':'\033[1;32;40m',
     'pg':'\033[4;34;47m',
     'nc':'\033[7;36m',
     'gb':'\033[32;44m'}

jogo = jogo.upper()

lista = ['PEDRA', 'PAPEL', 'TESOURA']

escolha = random.choice(lista)
if jogo == 'PEDRA' and escolha == 'TESOURA':
    print('O computador escolheu {}{}{} e você {}{}{}, você ganhou!'
          .format(cor['bw'], escolha, cor['no'], cor['nc'], jogo, cor['no']))
    print('Pedra quebra tesoura!')
elif jogo == 'TESOURA' and escolha == 'PAPEL':
    print('O computador escolheu {}{}{} e você {}{}{}, você ganhou!'
          .format(cor['rb'], escolha, cor['no'], cor['nc'], jogo, cor['no']))
    print('Tesoura corta papel!')
elif jogo == 'PAPEL' and escolha == 'PEDRA':
    print('O computador escolheu {}{}{} e você {}{}{}, você ganhou!'
          .format(cor['gw'], escolha, cor['no'], cor['nc'], jogo, cor['no']))
    print('Papel embrulha pedra!')
elif jogo == escolha:
    print('O computador escolheu {}{}{} e você {}{}{}, vocês empataram!'
          .format(cor['pg'], escolha, cor['no'], cor['nc'], jogo, cor['no']))
else:
    print('O computador escolheu {}{}{} e você {}{}{}, você perdeu!'
          .format(cor['gb'], escolha, cor['no'], cor['nc'], jogo, cor['no']))
    if escolha == 'TESOURA' and jogo == 'PAPEL':
        print('Tesoura corta papel!')
    elif escolha == 'PEDRA' and jogo == 'TESOURA':
        print('Pedra quebra tesoura!')
    elif escolha == 'PAPEL' and jogo == 'PEDRA':
        print('Papel embrulha pedra!')

