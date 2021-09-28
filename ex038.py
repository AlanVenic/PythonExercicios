#escreva um programa q leia dois numeros inteiros e compare-os.
#mostrando uma das msgs:
# o primeiro valor é maior
#o segundo valor é maior
#os dois são iguais

print('Escolha dois números inteiros e irei compará-los.')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 < num2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, ambos são iguais.')
