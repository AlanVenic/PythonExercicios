#escreva programa q leia numero inteiro e peça para usuario escolher qual a base de conversão
import math

num = int(input('Digite um número decimal qualquer: '))
print('Qual será a base de conversão?\n'
                 '[1] Binário\n'
                 '[2] Octal\n'
                 '[3] Hexadecimal\n'
                 '[4] Para os três')
conv = int(input('Qual sua opção? '))


if conv == 1:
    print('O número {} convertido para binário fica {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O número {} convertido para octal fica {}.'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O número {} convertido para hexadecimal fica {}.'.format(num, hex(num)[2:]))
elif conv ==4:
    print('O número {} convertido para binário, octal e hexadecimal '
          'respectivamente fica {}, {}, {}.'.format(num, bin(num)[2:], oct(num)[2:], hex(num)[2:]))
else:
    print('Opção invalida, tente novamente.')