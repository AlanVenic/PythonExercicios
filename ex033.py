#faça um programa que leia 3 numeros e mostre qual maior e qual menor
num1 = (int(input('Digite o primeiro número: ')))
num2 = (int(input('Digite o segundo número: ')))
num3 = (int(input('Digite o terceiro número: ')))
lista = [num1, num2, num3]
ordem = sorted(lista)
print('O maior número é {} e o menor número é {}.'.format(ordem[2], ordem[0]))

n1 = (int(input('Digite o primeiro número: ')))
n2 = (int(input('Digite o segundo número: ')))
n3 = (int(input('Digite o terceiro número: ')))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor valor é {}.'.format(menor))
print('O maior valor é {}.'.format(maior))