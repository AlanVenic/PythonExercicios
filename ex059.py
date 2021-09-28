#crie um programa q leia 2 valores e mostre um menu na tela
#[1]somar; [2]multiplicar; [3]maior; [4]novos numeros; [5]sair do programa
#o programa deve realizar a operação solicitada em cada caso

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''O que deseja fazer:
          [1]SOMAR
          [2]MULTIPLICAR
          [3]MAIOR
          [4]NOVOS NÚMEROS
          [5]SAIR''')
    opcao = int(input('Escolha uma das opções: '))
    if opcao == 1:
        print('A soma de {} e {} é igual a {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicação de {} por {} é igual a {}.'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O maior número dos dois é {}'.format(num1))
        else:
            print('O maior número dos dois é {}'.format(num2))
    elif opcao == 4:
        print('Informe os números novamente')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        ''
    else:
        print('Opção inválida, tente novamente.')
print('FIM DO PROGRAMA')
quit()



