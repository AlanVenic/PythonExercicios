#crie um programa q vai ler varios numeros e colocar numa lista. depois, crie duas listas extras
#que vão conter apenas valores pares e valores impares digitados, respectivamente
#ao final, mostre o conteudo das 3 listas geradas
#obs: criar a lista completa primeiro e depois gerar as 2 listas baseadas na lista completa

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
pares = []
impares = []

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
lista.sort()
print(f'Sua lista completa tem os seguintes valores: {lista}')
print(f'Sua lista de números pares é: {pares}')
print(f'Sua lista de números ímpares é: {impares}')
