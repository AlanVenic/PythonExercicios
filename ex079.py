#crie um programa onde o usuario possa digitar varios numeros e cadastre-os em uma lista.
#caso o numero ja exista na lista, ele não será adicionado. no final, serão exibidos tds os numeros
#unicos digitados em ordem crescente
#obs: a cada numero adicionado, perguntar se o usuario quer continuar

lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor duplicado não será adicionado a lista.')
    cont = str(input('Deseja continuar?[S/N] ')).upper().strip()
    while cont not in 'SN':
        print('Opção inválida.')
        cont = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if cont == 'N':
        break
print(f'Os números digitados em ordem crescente foram {sorted(lista)}')

