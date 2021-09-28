#crie um programa onde o usuario digite 5 numeros e cadastre-os numa lista,
#já na posição correta de inserção (sem usar o sort()) entre um numero menor e um maior.
# no final, mostre a lista ordenada na tela

lista = []

for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')