#elabore programa calcule valor a ser pago por produto considerando
#seu preço normal e condição de pagamento

print('FINALIZANDO COMPRA')
valor = float(input('Qual o valor do produto? '))
cond = int(input('Condições de pagamento:\n'
                 '[1] À vista (dinheiro ou cheque): 10% de desconto\n'
                 '[2] À vista no cartão: 5% de desconto\n'
                 '[3] Em até 5x no cartão: sem desconto\n'
                 '[4] 6x ou mais no cartão: 20% de juros\n'
                 'Escolha uma das opções: '))
if cond == 3:
    parce = int(input('Em quantas vezes você vai dividir? '))
    print('Seu produto vai custar {:.0f} parcelas de R${:.2f}, '
              'para o valor total de R${:.2f}.'.format(parce, valor/parce, valor))
elif cond == 4:
    parce1 = int(input('Em quantas vezes você vai dividir? '))
    print('Seu produto vai custar {:.0f} parcelas de R${:.2f} para '
          'o valor total de R${:.2f} com 20% de juros.'.format(parce1, (valor+(valor*0.2))/parce1, valor+(valor*0.2)))
elif cond == 1:
    print('O valor final do produto é R${:.2f} com 10% de desconto.'.format(valor-(valor*0.1)))
else:
    print('O valor final do produto é R${:.2f} com 5% de desconto.'.format(valor-(valor*0.05)))
