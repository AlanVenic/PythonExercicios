#faça um programa q tenha uma função maior() q receba varios parametros inteiros
#seu programa deve ser capaz de avaliar tds os valores e mostrar os valores e definir o maior

from time import sleep

def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores digitados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} números ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(5, 10, 11, 34, 12, 1459, 46, 2)
