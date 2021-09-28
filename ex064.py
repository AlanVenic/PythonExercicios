#crie um programa que leia varios numeros inteiros. o programa so vai parar
#quando o usuario digitar o valor 999. no final, mostre qnts numeros foram digitados
#e qual soma entre eles (desconsiderando o 999)


print('SÓ PARA COM 999')
num = 0
lista = []
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        lista.insert(1, num)
soma = sum(lista)
list = str(lista)[1:-1]
print('Foram digitados os números {}'.format(list))
print('A soma dos números digitados é {}'.format(soma))

num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
print('FIM')
