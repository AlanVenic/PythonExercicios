#crie um programa q simule o funcionamento de um caixa eletronico.
#no inicio perungte ao usuario o valor a ser sacado(numero inteiro)
#o programa vai informar qnts cedulas de cada valor serao entregues
#obs: considere q o caixa tem cedulas de 50, 20, 10 e 1 real

print('CAIXA ELETRÔNICO')
print('''Quanto você deseja sacar? 
Cédulas disponíveis: R$ 100,00, R$50,00, 
R$20,00, R$10,00, R$5,00 e R$1,00''')
valor = int(input('Digite o valor: '))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Volte sempre!')
