#crie um programa q tenha função fatorial() q receba 2 parametros: primeiro indica numero a calcular
#e o outro chamado show, q será um valor logico(opcional) indicando se sera mostrado ou nao na tela
#o processo de calculo do fatorial

def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
        f *= c
    return f


print(fatorial(5, show=True))

num = int(input('Qual número quer saber o fatorial: '))
print(f'O fatorial de {num} é igual a {fatorial(num)}.')
opc = str(input('Deseja ver o processo de cálculo? [S/N] ')).upper()
if opc == 'S':
    print(f'O cálculo é {num}!: ', end='')
    fatorial(num, show=True)




