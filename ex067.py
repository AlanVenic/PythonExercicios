#faça um programa q mostre a tabuada de varios numeros, um de cada vez
#para cada valor digitado. o programa para qnd o numero for negativo

print('TABUADA')
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
print('FIM')
