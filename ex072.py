#crie um programa q tenha uma tupla totalmente preenchida com uma contagem escrito
#por extenso de 0 a 20. seu programa deve ler um numero (entre 0 e 20) e mostrar por extenso

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
       esc = int(input('Digite um número de 0 a 20: '))
       if 0 <= esc <= 20:
              break
       print('O valor digitado é inválido.')
print(f'Você digitou o número {num[esc]}.')
