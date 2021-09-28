#crie um programa q leia varios numeros inteiros. no final da execução, mostre
#a media entre os numeros e qual o maior e o menor. o programa deve perguntar
#ao usuario se ele quer ou nao continuar a digitar valores

print('A MÉDIA')
lista = []
base = 0
cont = ''
while cont != 'N':
    num = int(input('Digite um valor: '))
    lista.insert(1, num)
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    base += 1
    if cont != 'N':
        ''
media = sum(lista)/base
list.sort(lista)
print('A média dos números digitados é {}.'.format(media))
print('O maior valor é {} e o menor valor é {}.'.format(lista[0], lista[-1]))

num = 0
resp = 'S'
soma = qnt = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    qnt += 1
    if qnt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma/qnt
print('Você digitou {} números e a média foi {:.2f}.'.format(qnt, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
print('Acabou')
