#crie um programa q vai ler varios numeros e colocar numa lista. depois disso mostre:
#qnts numeros foram digitados; a lista em ordem decrescente; se o valor 5 foi digitado e esta ou nao na lista
#obs: perguntar se o usuario quer continuar ou nao

lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont = str(input('Deseja continuar?[S/N] ')).upper().strip()
    while cont not in 'SN':
        print('Opção inválida.')
        cont = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if cont == 'N':
        break
lista.sort(reverse=True)
if 5 in lista:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')
print(f'Os números digitados em ordem decrescente foram {lista}')
print(f'Foram digitados {len(lista)} números.')